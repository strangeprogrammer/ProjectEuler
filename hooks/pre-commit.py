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
	
	if subprocess.run([
		'make', '--silent', '.result.txt',
	], cwd = cwd).returncode != 0:
		return [int(number), False]
	
	x = subprocess.run([
		'cat', '.result.txt',
	], cwd = cwd, stdout = subprocess.PIPE)
	
	return [
		int(number),
		x.returncode == 0 and x.stdout == tobytes(answer + '\n')
	]

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
