import unittest
from fib_sum_even_fibonacci import *


# run this by typing python -m unittest 

class TestFibFunctionMethods(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(fib_sum_even_fibonacci(400), 798)



        