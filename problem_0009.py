#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a² + b² = c²
For example, 3² + 4² = 9 + 16 = 25 = 5²

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import sys
import timer
import unittest

class Problem0009():
    def is_pythagorean_triplet(self, a, b, c):
        return (pow(a, 2) + pow(b, 2)) == pow(c, 2)

    def get_product_a_b_c_when_sum_equals_n(self, n):
        a = 1
        b = 2
        c = 3
        while a + b + c <= n:
            if (pow(a, 2) + pow(b, 2)) <= pow(c, 2):
                while a < b:
                    if self.is_pythagorean_triplet(a, b, c) and a + b + c == n:
                        return a * b * c
                    else:
                        a += 1
                b += 1
                a = 1
            else:
                c += 1
                a = 1
                b = 2

    def run(self):
        print 'The product of abc when a² + b² = c² and a + b + c = 1000 is %i'\
            % (self.get_product_a_b_c_when_sum_equals_n(1000))

class TestProductABC(unittest.TestCase):
    def setUp(self):
        self.problem_0009 = Problem0009()

    def test_product_abc_for_sum_12(self):
        self.assertEqual(self.problem_0009.\
            get_product_a_b_c_when_sum_equals_n(12), 60)

    def test_pythagorean_triplet(self):
        self.assertEqual(self.problem_0009.is_pythagorean_triplet(3, 4, 5),\
            True)
        self.assertEqual(self.problem_0009.is_pythagorean_triplet(3, 4, 6),\
            False)
        self.assertEqual(self.problem_0009.is_pythagorean_triplet(5, 12, 13),\
            True)

if __name__ == '__main__':
    if 'test' in sys.argv:
        sys.argv.remove('test')
        unittest.main()
    else:
        problem0009 = Problem0009()
        with timer.Timer() as problem_timer:
            problem0009.run()
