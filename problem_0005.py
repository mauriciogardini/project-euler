#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

import sys
import timer
import unittest

class Problem0005():
    def smallest_number_divisible_by_1_to_n(self, n):
        divisors = range(n, 0, -1)
        divisible_by_all = False
        dividend = 0
        while not divisible_by_all:
            dividend += n
            divisible_by_all = all(dividend % divisor == 0\
                for divisor in divisors)
        return dividend

    def run(self):
        print 'The smallest positive number that is divisible from 1 to 20 '\
        'is %i' % self.smallest_number_divisible_by_1_to_n(20)

class TestSmallestPositiveNumberDivisible(unittest.TestCase):
    def setUp(self):
        self.problem_0005 = Problem0005()

    def test_smallest_positive_number_divisible_1_to_10(self):
        self.assertEqual(self.problem_0005.\
            smallest_number_divisible_by_1_to_n(10), 2520)

if __name__ == '__main__':
    if 'test' in sys.argv:
        sys.argv.remove('test')
        unittest.main()
    else:
        problem0005 = Problem0005()
        with timer.Timer() as problem_timer:
            problem0005.run()
