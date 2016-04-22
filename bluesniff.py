import bluetooth as bt
from time import gmtime, strftime

devices = {}

while True:
	time = strftime("[ %Y-%m-%d | %H:%M:%S ]", gmtime())
	addrs = bt.discover_devices(duration=5,flush_cache=True)

	removed = set( list( devices.keys() ) ) - set( addrs )
	for remove in removed:
		print( time, remove, "'", devices[ remove ], "' has gone poof!" )
		del devices[ remove ]

	for addr in addrs:
		name = bt.lookup_name( addr )
		if not addr in devices.keys():
			print( time, addr, "'", name, "' has been found!" )
			for s in bt.find_service( address = addr ):
				print( "\t\t > ", name, " has '", s[ "name" ], "' service." )
			devices[ addr ] = name
		else:
			if not devices[ addr ] == name:
				print( time, addr, "'", devices[ addr ], "' has changed its name to '", name, "'" )
				devices[ addr ] = name
