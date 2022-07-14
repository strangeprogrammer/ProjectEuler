#!/usr/bin/env python3

import sys
import os
from os import path
from multiprocessing import Pool
import subprocess

gwt = os.getenv('GIT_WORK_TREE')
if gwt is None:
	raise Exception("Environment variable 'GIT_WORK_TREE' wasn't set...")

def tobytes(s):
	return bytes(map(ord, s))

def grader(t):
	global gwt
	[number, answer] = t
	
	cwd = path.join(
		gwt,
		'answers',
		number,
	)
	
	x = subprocess.run([
		path.join(cwd, 'answer.py')
	], cwd = cwd, stdout = subprocess.PIPE)
	
	return [int(number), x.stdout == tobytes(answer + '\n')]

def main():
	global gwt
	
	answers = []
	with open(
		path.join(gwt, 'answers.txt'),
	'r') as fp:
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
