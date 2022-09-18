#!/usr/bin/env python3

# We shall begin by defining a set of numbers as an n:cluster iff that set of numbers contains exactly 'n' elements, each pair of which obeys the cluster predicate as stated in the original problem.
# The problem is essentially asking us to find the 5:cluster with the lowest sum of its elements.
# Note that, for any n:cluster, every 'n-1' sized subset of that cluster is an n-1:cluster.
# Thus, in the process of generating every n:cluster, we can also generate n+1:clusters accurately whenever 2 specific candidate n:clusters, which will each differ by 1 common element from a target n+1:cluster, are found.
# Upon these 2 candidate n:clusters, we will test whether the predicate returns True for their 2 differing elements. If it does, the union of these n:clusters will indeed be a new n+1:cluster.

# For programmatic simplicity, we define all the 1:clusters as the sets which contain only a single prime number.
# Additionally, in order to find pairs of candidate clusters faster, for every n:cluster, we keep track of the candidate clusters used to create it and the n+1:clusters that it was used to create.

# TODO : Keep track of every subcluster, not just the candidate clusters used to create it?

# Caveat: unfortunately, I don't yet know a way to *prove* that the first 5-cluster encountered is that which (essentially) solves the problem, only that this answer is accepted by Project Euler as correct.

from primes import primes

def predicate(x, y):
	if	int(str(x) + str(y)) in primes \
	and	int(str(y) + str(x)) in primes:
		return True
	else:
		return False

class cluster(set):
	def __init__(self, iterable, *subclusters):
		self.subclusters = set(subclusters)
		for subcluster in subclusters:
			subcluster.superclusters |= {self}
		
		self.superclusters = set()
		
		super().__init__(iterable)
	
	def __hash__(self):
		return hash(tuple(sorted(self)))

zerocluster = cluster(set())

oneclusters = set()
def get1clusters():
	global zerocluster, oneclusters
	for [index, prime] in enumerate(primes):
		new = cluster({prime}, zerocluster)
		oneclusters |= {new}
		yield new

def clusterfactory(prevgen):
	nclusters = set()
	
	def getnclusters():
		nonlocal prevgen, nclusters
		for this in prevgen():
			for subcluster in this.subclusters:
				for sibling in subcluster.superclusters:
					if sibling is this:
						continue
					elif sibling == this: # Edge case to deal with the existence of more than 1 way to create the next-level cluster
						sibling.subclusters |= this.subclusters
						sibling.superclusters |= this.superclusters
						continue
					diff = this ^ sibling
					if predicate(diff.pop(), diff.pop()):
						new = cluster(this | sibling, this, sibling)
						nclusters |= {new}
						yield new
	
	return getnclusters

get2clusters = clusterfactory(get1clusters)
get3clusters = clusterfactory(get2clusters)
get4clusters = clusterfactory(get3clusters)
get5clusters = clusterfactory(get4clusters)

def main():
	return sum(next(get5clusters()))

print(main())
