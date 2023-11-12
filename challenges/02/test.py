#!/usr/bin/env python3

from decode_message import decode_message

import unittest

class Test01(unittest.TestCase):

    def test1(self):
        """
        Test 1
        """

        self.assertEqual(decode_message('##*&'),'4')

    def test2(self):
        """
        Test 2
        """

        self.assertEqual(decode_message('&##&*&@&'),'0243')

if __name__ == '__main__':
    unittest.main()