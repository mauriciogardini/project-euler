#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import sys
import timer
import unittest

class Problem0004():
    def largest_palindrome_product_n_digit_numbers(self, n):
        largest_palindrome = -1
        for i in range(int('1' + ((n -1) * '0')), int('9' * n) + 1):
            for j in range(int('1' + ((n -1) * '0')), int('9' * n) + 1):
                largest_palindrome = i * j if str(i * j) == str(i * j)[::-1] and\
                    i * j > largest_palindrome else largest_palindrome
        return largest_palindrome

    def run(self):
        print 'The largest palindrome made from the product of two 3-digit '\
        'numbers is %i' % self.largest_palindrome_product_n_digit_numbers(3)

class TestLargestPrimeFactor(unittest.TestCase):
    def setUp(self):
        self.problem_0004 = Problem0004()

    def test_sum_even_fibonacci_numbers_under_100(self):
        self.assertEqual(self.problem_0004.\
            largest_palindrome_product_n_digit_numbers(2), 9009)

if __name__ == '__main__':
    if 'test' in sys.argv:
        sys.argv.remove('test')
        unittest.main()
    else:
        problem0004 = Problem0004()
        with timer.Timer() as problem_timer:
            problem0004.run()
