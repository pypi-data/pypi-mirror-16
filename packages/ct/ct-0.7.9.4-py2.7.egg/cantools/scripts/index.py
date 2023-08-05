"""
### Usage: ctindex [--mode=MODE] [--domain=DOMAIN] [--port=PORT]

### Options:
	-h, --help            show this help message and exit
	-m MODE, --mode=MODE  may be: 'refcount' (default - count up all foreignkey
	                      references for sort orders and such) or 'index'
	                      (assign each record a sequential integer index). Note
	                      regarding 'index' mode: it _must_ happen remotely;
	                      it's generally unnecessary unless you're trying to
	                      migrate an unindexed database away from gae and need
	                      an index/key per record; it should be invoked from
	                      _outside_ -- that's right, outside -- of your
	                      project's directory (to avoid loading up a bunch of
	                      google network tools that may be crappy or cause
	                      issues outside of their normal 'dev_appserver'
	                      environment
	-d DOMAIN, --domain=DOMAIN
	                      ('index' mode only) what's the domain of the target
	                      server? (default: localhost)
	-p PORT, --port=PORT  ('index' mode only) what's the port of the target
	                      server? (default: 8080)

As you can see, this script's behavior changes according to the backend of the target project.

### dez
Run this if your CTRefCount records get messed up for
some reason. It will go through and recount everything.

### gae
Run this on a database with lots of missing index values.
"""

from getpass import getpass
from optparse import OptionParser
from cantools.util import error, log, batch
from cantools.db import get_schema, get_model, put_multi
from cantools.web import fetch
from cantools import config
if config.web.server == "dez":
	from cantools.db import session, func, refresh_counter

counts = { "_counters": 0 }

#
# dez
#

def get_keys(kind, reference):
	log("acquiring %s (%s) keys"%(kind, reference), 1)
	mod = get_model(kind)
	q = session.query(getattr(mod, "key"))
	qcount = q.count()
	log("found %s"%(qcount,), 2)
	fname, fkey = reference.split(".")
	fmod = get_model(fname)
	fprop = getattr(fmod, fkey)
	sub = session.query(fprop, func.count("*").label("sub_count")).group_by(fprop).subquery()
	q = q.join(sub, mod.key==getattr(sub.c, fkey))
	newcount = q.count()
	log("filtering out %s untargetted entities"%(qcount - newcount), 2)
	qcount = newcount
	log("returning %s keys"%(qcount,), 2)
	return q.all()

def refmap():
	log("compiling back reference map")
	rmap = {}
	for tname, schema in get_schema().items():
		for pname, kinds in schema["_kinds"].items():
			reference = "%s.%s"%(tname, pname)
			counts[reference] = 0
			for kind in [k for k in kinds if k != "*"]: # skip wildcard for now
				if kind not in rmap:
					rmap[kind] = {}
				rmap[kind][reference] = get_keys(kind, reference)
	return rmap

def do_batch(chunk, reference):
	log("refreshing %s %s keys"%(len(chunk), reference), 1)
	i = 0
	rc = []
	for item in chunk: # item is single-member tuple
		rc.append(refresh_counter(item[0], reference))
		i += 1
		if not i % 100:
			log("processed %s"%(i,), 3)
	counts[reference] += len(chunk)
	counts["_counters"] += len(rc)
	log("refreshed %s total"%(counts[reference],), 2)
	log("updated %s counters"%(counts["_counters"],), 2)
	put_multi(rc)
	log("saved", 2)

def refcount():
	log("indexing foreignkey references throughout database", important=True)
	import model # load schema
	for kind, references in refmap().items():
		log("processing table: %s"%(kind,), important=True)
		for reference, keys in references.items():
			batch(keys, do_batch, reference)
	tcount = sum(counts.values()) - counts["_counters"]
	log("refreshed %s rows and updated %s counters"%(tcount, counts["_counters"]), important=True)

#
# gae
#

def index(host, port):
	pw = getpass("what's the admin password? ")
	log("indexing db at %s:%s"%(host, port), important=True)
	log(fetch(host, "/_db?action=index&pw=%s"%(pw,), port))
#	log("acquiring schema")
#	schema = fetch(host, "/_db?action=schema", port, ctjson=True)
#	for kind in schema:
#		log(fetch(host, "/_db?action=index&pw=%s&kind=%s"%(pw, kind), port))

def go():
	parser = OptionParser("ctindex [--mode=MODE] [--domain=DOMAIN] [--port=PORT]")
	parser.add_option("-m", "--mode", dest="mode", default="refcount",
		help="may be: 'refcount' (default - count up all foreignkey references for sort orders "
			"and such) or 'index' (assign each record a sequential integer index). "
			"Note regarding 'index' mode: it _must_ happen remotely; it's generally "
			"unnecessary unless you're trying to migrate an unindexed database away from "
			"gae and need an index/key per record; it should be invoked from _outside_ "
			"-- that's right, outside -- of your project's directory (to avoid loading "
			"up a bunch of google network tools that may be crappy or cause issues outside "
			"of their normal 'dev_appserver' environment")
	parser.add_option("-d", "--domain", dest="domain", default="localhost",
		help="('index' mode only) what's the domain of the target server? (default: localhost)")
	parser.add_option("-p", "--port", dest="port", default="8080",
		help="('index' mode only) what's the port of the target server? (default: 8080)")
	options, args = parser.parse_args()

	log("mode: %s"%(options.mode,), important=True)
	if options.mode == "refcount":
		refcount()
	elif options.mode == "index":
		index(options.domain, int(options.port))
	else:
		error("unknown mode: %s"%(options.mode,))
	log("goodbye")

if __name__ == "__main__":
	go()