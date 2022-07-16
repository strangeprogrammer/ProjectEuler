#!/usr/bin/env python3

import sys
import os
from os import path
from multiprocessing import Pool
import subprocess

top = os.getcwd()

def tobytes(s):
	return bytes(map(ord, s))

def grader(t):
	global top
	[number, answer] = t
	
	cwd = path.join(
		top,
		'answers',
		number,
	)
	
	x = subprocess.run([
		path.join(cwd, 'answer.py')
	], cwd = cwd, stdout = subprocess.PIPE)
	
	return [int(number), x.stdout == tobytes(answer + '\n')]

def main():
	global top
	
	answers = []
	with open(path.join(top, 'answers.txt'), 'r') as fp:
		answers = fp.readlines()
	
	answers = list(map(
		lambda s: s.strip().split(),
		answers
	))
	
	with Pool(len(answers)) as p:
		results = p.map(grader, answers)
	
	retval = 0
	for [i, result] in results:
		if not result:
			print("Error: 'answer.py' for problem '%d' returned the wrong result..." % i, file=sys.stderr)
			retval = 1
	
	return retval

sys.exit(main())
