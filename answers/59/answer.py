#!/usr/bin/env python3

import itertools
import json

from gentools import indexable, lazylenge

filename = 'p059_cipher.txt'
dictname = 'words_dictionary.json'
alphas = list(range(ord('a'), ord('z') + 1)) + [ord(' ')]

def getcontents():
	global filename
	with open(filename, 'r') as fd:
		return list(map(
			int,
			fd.read().split(',')
		))

def getdictionary():
	global dictname
	with open(dictname, 'r') as fd:
		return set(
			json.loads(fd.read()).keys()
		)

def spliterator(*args, **kwargs): # This function is necessary since (TMK) 'str.split' isn't lazy by default
	def wrapped(s, delims = ' '):
		previ = 0
		for [i, c] in enumerate(s):
			if c in delims:
				yield s[previ:i]
				previ = i + 1 # Skip the previous delimiter
		
		yield s[previ:len(s)] # Yield the final item
	
	return filter(
		lambda s: 0 < len(s),
		wrapped(*args, **kwargs)
	)

def decrypt(s, kt):
	for [c, ki] in zip(s, itertools.cycle(kt)):
		yield chr(c ^ ki)

def decruft(s):
	global alphas
	
	return filter(
		lambda c: ord(c.lower()) in alphas,
		s
	)

def main():
	global alphas
	
	contents = getcontents()
	dictionary = getdictionary()
	
	for key in itertools.product(alphas, alphas, alphas):
		plaintext = indexable(decruft(decrypt(contents, key)))
		
		if lazylenge(150, filter(
			lambda w: ''.join(w).lower() in dictionary,
			spliterator(plaintext)
		)):
			candidate = decrypt(contents, key)
			prefix = next(candidate) + next(candidate) + next(candidate)
			
			if prefix == 'An ': # This short prefix was obtained by manually scanning through results
				return sum(map(
					ord,
					prefix + ''.join(candidate)
				))

print(main())
