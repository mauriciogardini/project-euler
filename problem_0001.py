#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import sys
import unittest

class Problem0001():
    def sum_multiples_below_n(self, n):
        return sum([number for number in range(1, n) if number % 3 == 0 or\
            number % 5 == 0])

    def run(self):
        print 'The sum of all the multiples of 3 and 5 below 1000 equals %i' %\
            (self.sum_multiples_below_n(1000))

class TestSumMultiples(unittest.TestCase):
    def setUp(self):
        self.problem_0001 = Problem0001()

    def test_sum_10(self):
        self.assertEqual(self.problem_0001.sum_multiples_below_n(10), 23)

if __name__ == '__main__':
    if 'test' in sys.argv:
        sys.argv.remove('test')
        unittest.main()
    else:
        problem0001 = Problem0001()
        problem0001.run()
