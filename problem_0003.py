#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import sys
import timer
import unittest

class Problem0003():
    def largest_prime_factor_n(self, n):
        divisor = 1
        while n != 1:
            divisor += 1
            n = n / divisor if self.is_prime(divisor) and n % divisor == 0\
                else n
        return divisor

    def is_prime(self, n):
        for number in range(2, (n/2) + 1):
            if n % number == 0:
                return False
        return True

    def run(self):
        print 'The largest prime factor of 600851475143 is %i' %\
            (self.largest_prime_factor_n(600851475143))

class TestLargestPrimeFactor(unittest.TestCase):
    def setUp(self):
        self.problem_0003 = Problem0003()

    def test_sum_even_fibonacci_numbers_under_100(self):
        self.assertEqual(self.problem_0003.\
            largest_prime_factor_n(13195), 29)

    def test_n_is_prime(self):
        self.assertEqual(self.problem_0003.is_prime(13), True)
        self.assertEqual(self.problem_0003.is_prime(14), False)
        self.assertEqual(self.problem_0003.is_prime(61), True)
        self.assertEqual(self.problem_0003.is_prime(64), False)

if __name__ == '__main__':
    if 'test' in sys.argv:
        sys.argv.remove('test')
        unittest.main()
    else:
        problem0003 = Problem0003()
        with timer.Timer() as problem_timer:
            problem0003.run()
