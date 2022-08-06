#!/usr/bin/env python3

filename = 'p054_poker.txt'

def genmatches():
	global filename
	
	with open(filename, 'r') as fp:
		lines = fp.readlines()
	
	for line in lines:
		line = line.strip()
		cards = line.split(' ')
		yield [
			cards[:5],
			cards[5:],
		]

def makecard(s):
	return {
		'rank': {
			'2':2,
			'3':3,
			'4':4,
			'5':5,
			'6':6,
			'7':7,
			'8':8,
			'9':9,
			'T':10,
			'J':11,
			'Q':12,
			'K':13,
			'A':14,
		}[s[0]],
		'suit': {
			'D':0,
			'H':1,
			'C':2,
			'S':3,
		}[s[1]],
	}

def preparehand(hand):
	return sorted(
		map(makecard, hand),
		key = lambda card: card['rank']
	)

def formOAKs(hand):
	hand = hand.copy()
	groups = []
	
	while 0 < len(hand):
		against = hand.pop()
		groups += [[against]]
		for card in hand.copy():
			if card['rank'] == against['rank']:
				hand.remove(card)
				groups[-1] += [card]
	
	return groups

def extractnOAK(groups, n):
	matches = list(filter(
		lambda group: len(group) == n,
		groups
	))
	
	notmatches = list(filter(
		lambda group: len(group) != n,
		groups
	))
	
	return [matches, notmatches]

def determine4OAK(groups):
	[found, leftovers] = extractnOAK(groups, 4)
	if len(found) == 1:
		degree = found[0][0]['rank']
	else:
		degree = 0
	return {
		'found?': len(found) == 1,
		'degree': degree,
		'leftovers': leftovers,
	}

def determine3OAK(groups):
	[found, leftovers] = extractnOAK(groups, 3)
	if len(found) == 1:
		degree = found[0][0]['rank']
	else:
		degree = 0
	return {
		'found?': len(found) == 1,
		'degree': degree,
		'leftovers': leftovers,
	}

def determinepairs(groups):
	[found, leftovers] = extractnOAK(groups, 2)
	if len(found) == 1:
		degree = found[0][0]['rank']
	elif len(found) == 2:
		degree = max([
			found[0][0]['rank'],
			found[1][0]['rank'],
		])
	else:
		degree = 0
	return {
		'numfound': len(found),
		'degree': degree,
		'leftovers': leftovers,
	}

def determinestraight(hand):
	ranks = sorted(map(
		lambda card: card['rank'],
		hand
	))
	
	if ranks[0] + 1 == ranks[1]	\
	and ranks[1] + 1 == ranks[2]	\
	and ranks[2] + 1 == ranks[3]	\
	and ranks[3] + 1 == ranks[4]:
		return {
			'found?': True,
			'degree': ranks[4],
		}
	else:
		return {
			'found?': False,
			'degree': 0,
		}

def determineflush(hand):
	suits = list(map(
		lambda card: card['suit'],
		hand
	))
	
	if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
		return {
			'found?': True,
			'degree': max(map(
				lambda card: card['rank'],
				hand
			)),
		}
	else:
		return {
			'found?': False,
			'degree': 0,
		}

def ranktochr(rank):
	return chr(rank + ord('A'))

def formdegree(result):
	return ranktochr(result['degree'])

def formhigh(leftovers):
	return ''.join(
		sorted(
			list(map(
				lambda t: ranktochr(t[0]['rank']),
				leftovers
			)), reverse = True
		)
	)

def getscore(hand):
	resultflush = determineflush(hand)
	resultstraight = determinestraight(hand)
	
	if resultstraight['found?'] and resultflush['found?']:
		if resultstraight[4] == 14:
			return 'J'
		else:
			return 'I' + formdegree(resultstraight)
	elif resultflush['found?']:
		return 'F' + formdegree(resultflush)
	elif resultstraight['found?']:
		return 'E' + formdegree(resultstraight)
	else:
		OAKs = formOAKs(hand)
		
		result4OAK = determine4OAK(OAKs)
		result3OAK = determine3OAK(OAKs)
		resultpairs = determinepairs(OAKs)
		
		if result4OAK['found?']:
			return 'H' + formdegree(result4OAK) + formhigh(result4OAK['leftovers'])
		elif result3OAK['found?']:
			if resultpairs['numfound'] == 1:
				return 'G' + formdegree(result3OAK)
			else:
				return 'D' + formdegree(result3OAK) + formhigh(result3OAK['leftovers'])
		elif resultpairs['numfound'] == 2:
			return 'C' + formdegree(resultpairs) + formhigh(resultpairs['leftovers'])
		elif resultpairs['numfound'] == 1:
			return 'B' + formdegree(resultpairs) + formhigh(resultpairs['leftovers'])
		else:
			return 'A' + formhigh(resultpairs['leftovers'])

def main():
	total = 0
	for [handa, handb] in genmatches():
		handa = preparehand(handa)
		handb = preparehand(handb)
		if getscore(handa) > getscore(handb):
			total += 1
	
	return total

print(main())
