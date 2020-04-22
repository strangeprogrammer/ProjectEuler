#!/bin/sed -e 3q;d;

# Do not run this file directly - include it instead

def mu(predicate, iterable):
	for n, e in enumerate(iterable):
		if predicate(e):
			return n
	return None
