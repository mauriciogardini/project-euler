#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?
"""

import sys
import timer
import unittest

class Problem0007():
    def nth_prime_number(self, n):
        number = 1
        while n !=0:
            number += 1
            if self.is_prime(number):
                n -= 1
        return number

    def is_prime(self, n):
        for number in range(2, (n/2) + 1):
            if n % number == 0:
                return False
        return True

    def run(self):
        print 'The 10001st prime number is %i' %\
            self.nth_prime_number(10001)

class TestPrimeNumber(unittest.TestCase):
    def setUp(self):
        self.problem_0007 = Problem0007()

    def test_6th_prime_number(self):
        self.assertEqual(self.problem_0007.nth_prime_number(6), 13)

if __name__ == '__main__':
    if 'test' in sys.argv:
        sys.argv.remove('test')
        unittest.main()
    else:
        problem0007 = Problem0007()
        with timer.Timer() as problem_timer:
            problem0007.run()
