#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Find the greatest product of five consecutive digits in the 1000-digit number.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
"""

import sys
import timer
import unittest

class Problem0008():
    def greatest_product_five_consecutive_digits(self, n):
        str_number = str(n)
        greater_product = 0
        while len(str_number) >= 5:
            product = eval('%s * %s * %s * %s * %s' %\
                (str_number[0], str_number[1], str_number[2], str_number[3],\
                str_number[4]))
            greater_product = product if product > greater_product\
                else greater_product
            str_number = str_number[1:]
        return greater_product

    def run(self):
        number = int('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' %\
            ('73167176531330624919225119674426574742355349194934',
            '96983520312774506326239578318016984801869478851843',
            '85861560789112949495459501737958331952853208805511',
            '12540698747158523863050715693290963295227443043557',
            '66896648950445244523161731856403098711121722383113',
            '62229893423380308135336276614282806444486645238749',
            '30358907296290491560440772390713810515859307960866',
            '70172427121883998797908792274921901699720888093776',
            '65727333001053367881220235421809751254540594752243',
            '52584907711670556013604839586446706324415722155397',
            '53697817977846174064955149290862569321978468622482',
            '83972241375657056057490261407972968652414535100474',
            '82166370484403199890008895243450658541227588666881',
            '16427171479924442928230863465674813919123162824586',
            '17866458359124566529476545682848912883142607690042',
            '24219022671055626321111109370544217506941658960408',
            '07198403850962455444362981230987879927244284909188',
            '84580156166097919133875499200524063689912560717606',
            '05886116467109405077541002256983155200055935729725',
            '71636269561882670428252483600823257530420752963450'))
        print 'The greatest product of five consecutive numbers is %i' %\
            self.greatest_product_five_consecutive_digits(number)

class TestGreatestProductFiveConsecutiveNumbers(unittest.TestCase):
    def setUp(self):
        self.problem_0008 = Problem0008()
        self.sequence = 1234567890

    def test_greatest_product_five_consecutive_numbers(self):
        self.assertEqual(self.problem_0008.\
            greatest_product_five_consecutive_digits(self.sequence), 15120)

if __name__ == '__main__':
    if 'test' in sys.argv:
        sys.argv.remove('test')
        unittest.main()
    else:
        problem0008 = Problem0008()
        with timer.Timer() as problem_timer:
            problem0008.run()