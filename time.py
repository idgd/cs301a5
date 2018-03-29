import insertion
import bubble
import selection
import merge

from time import time
from random import shuffle

# likely mergesort will have the best runtime, as theoretically it's O(n log(n)) < O(n^2) of the rest

def bench(f,l):
	a = 0
	c = 8
	for g in range(c):
		shuffle(l)

		# many repeated runs of sort algos are exponentially faster
		# most likely because of runtime optimizations
		# with this, time averages are much closer to individual run times
		flush = [f for f in range(111111)]
		shuffle(flush)
		flush.sort()

		s = time()
		f(l)
		e = time()

		a += (e - s)

	return(a / c)

l = [f for f in range(16384)]

t = bench(insertion.insertion,l)
print("Insertion time: {0:.8f}".format(t))

t = bench(bubble.bubble,l)
print("Bubble time:    {0:.8f}".format(t))

t = bench(selection.selection,l)
print("Selection time: {0:.8f}".format(t))

t = bench(merge.merge,l)
print("Merge time:     {0:.8f}".format(t))

# benchmark results:
# Insertion time: 0.69230759
# Bubble time:    0.00000831
# Selection time: 0.00000817
# Merge time:     0.00000638
# as expected, merge is the fastest, but surprisingly,
# only by a slim margin over selection sort
# insertion is also many orders of magnitude slower
