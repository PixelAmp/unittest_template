import unittest
from fib_sum_even_fibonacci import *

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertEqual(fib_sum_even_fibonacci(400), 798)

        