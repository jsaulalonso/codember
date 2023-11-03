#!/usr/bin/env python3

from decode_message import *

import unittest

class Test01(unittest.TestCase):

    def test1(self):
        """
        Test 1
        """

        self.assertEqual(decode_message('llaveS casa CASA casa llaves'),'llaves2casa3')

    def test2(self):
        """
        Test 2
        """

        self.assertEqual(decode_message('taza ta za taza'),'taza2ta1za1')

    def test3(self):
        """
        Test 3
        """

        self.assertEqual(decode_message('casas casa casasas'),'casas1casa1casasas1')

if __name__ == '__main__':
    unittest.main()