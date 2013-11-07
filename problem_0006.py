#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

import sys
import timer
import unittest

class Problem0006():
    def difference_between_sum_squares_minus_square_sums_of_n(self, n):
        square_sums = 0
        sum_squares = 0
        for number in xrange(1, n + 1):
            square_sums += number
            sum_squares += number * number
        square_sums *= square_sums
        return square_sums - sum_squares

    def run(self):
        print 'The difference between the sum of squares minus the square of '\
        'sums of the first 100 numbers is %i' %\
        self.difference_between_sum_squares_minus_square_sums_of_n(100)

class TestDifferenceSumSquaresSquareNumbers(unittest.TestCase):
    def setUp(self):
        self.problem_0006 = Problem0006()

    def test_difference_sum_squares_square_sums_10(self):
        self.assertEqual(self.problem_0006.\
            difference_between_sum_squares_minus_square_sums_of_n(10), 2640)

if __name__ == '__main__':
    if 'test' in sys.argv:
        sys.argv.remove('test')
        unittest.main()
    else:
        problem0006 = Problem0006()
        with timer.Timer() as problem_timer:
            problem0006.run()
