import insertion
import bubble
import selection
import merge

from time import time
from random import shuffle

# likely mergesort will have the best runtime, as theoretically it's O(n log(n)) < O(n^2) of the rest

def bench(f,l):
	shuffle(l)
	s = time()
	f(l)
	e = time()
	return(e - s)

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
# Insertion time: 5.64335537
# Bubble time:    0.00000238
# Selection time: 0.00000119
# Merge time:     0.00000095
# as expected, merge is the fastest, but surprisingly,
# only by a slim margin over selection sort
# insertion is also many orders of magnitude slower
