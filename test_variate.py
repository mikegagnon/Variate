#!/usr/bin/env python

import unittest
from variate import Variate

def countsToProbabilities(counts):
    total = float(sum([pair[1] for pair in counts]))
    newCounts = []
    for pair in counts:
        newPair = (pair[0], pair[1] / total)
        newCounts.append(newPair)
    return newCounts

class TestVariate(unittest.TestCase):

    def setUp(self):
        self.tokens = [
            ("a", 1),
            ("b", 10),
            ("c", 3),
            ("d", 7),
            ("e", 8),
            ("f", 9),
            ("g", 1),
            ("h", 1),
            ("i", 1),
            ("j", 1),
            ("k", 1),
            ("l", 1),
            ("m", 1),
            ("n", 1),
            ("o", 1),
            ("p", 1)
            ]

    def test_get(self):

        for max_node_size in range(1, len(self.tokens) * 2):
            v = Variate(self.tokens, max_node_size)
            self.assertEqual(v.get(0), "a")
            self.assertEqual(v.get(1), "b")
            self.assertEqual(v.get(10), "b")
            self.assertEqual(v.get(11), "c")
            self.assertEqual(v.get(13), "c")
            self.assertEqual(v.get(14), "d")
            self.assertEqual(v.get(20), "d")
            self.assertEqual(v.get(21), "e")
            self.assertEqual(v.get(28), "e")
            self.assertEqual(v.get(29), "f")
            self.assertEqual(v.get(37), "f")
            self.assertEqual(v.get(38), "g")
            self.assertEqual(v.get(39), "h")
            self.assertEqual(v.get(40), "i")
            self.assertEqual(v.get(41), "j")
            self.assertEqual(v.get(42), "k")
            self.assertEqual(v.get(43), "l")
            self.assertEqual(v.get(44), "m")
            self.assertEqual(v.get(45), "n")
            self.assertEqual(v.get(46), "o")
            self.assertEqual(v.get(47), "p")
            self.assertRaises(ValueError, v.get, 48)

    def test_getRand(self):

        v = Variate(self.tokens, max_node_size=1)
        counts = {}
        trials = 1000000
        for i in range(0, trials):
            token = v.getRand()
            if token not in counts:
                counts[token] = 0
            counts[token] += 1

        actual_prob = countsToProbabilities(sorted(counts.items()))
        expected_prob = countsToProbabilities(sorted(self.tokens))
        for (actual, expected) in zip(actual_prob, expected_prob):
            self.assertAlmostEqual(actual[1], expected[1], delta=0.002)

        

if __name__ == '__main__':
    unittest.main()