#! ust/bin/env python3
# coding: utf-8

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Testing Calculator"""

    def setUp(self):
        self._calc = Calculator()

    def test_addition(self):
        result = self._calc.addition(8, 7)
        self.assertEqual(result, 15)


unittest.main()
