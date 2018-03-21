import unittest
import insertion
import bubble
import selection
import merge

from random import shuffle

class TestSort(unittest.TestCase):

	def test_insert(self):
		l = [f for f in range(16)]
		t = l[:]
		shuffle(l)
		self.assertEqual(insertion.insertion(l),t)

	def test_bubble(self):
		l = [f for f in range(16)]
		t = l[:]
		shuffle(l)
		self.assertEqual(bubble.bubble(l),t)

	def test_selection(self):
		l = [f for f in range(16)]
		t = l[:]
		shuffle(l)
		self.assertEqual(selection.selection(l),t)

	def test_merge(self):
		l = [f for f in range(16)]
		t = l[:]
		shuffle(l)
		self.assertEqual(merge.merge(l),t)

unittest.main()
