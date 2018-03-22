import unittest
import insertion
import bubble
import selection
import merge

from itertools import permutations

class TestSort(unittest.TestCase):
	def bench(self,f):
		l = [f for f in range(9)]
		for g in permutations(l):
			self.assertEqual(f(list(g)),l)

	def test_insert(self):
		self.bench(insertion.insertion)

	def test_bubble(self):
		self.bench(bubble.bubble)

	def test_selection(self):
		self.bench(selection.selection)

	def test_merge(self):
		self.bench(merge.merge)

unittest.main()
