# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
        self.assertAlmostEqual(postfix_eval("10 5 *"), 50)
        self.assertAlmostEqual(postfix_eval("30 6 /"), 5)
        self.assertAlmostEqual(postfix_eval("5 2 **"), 25)
        self.assertAlmostEqual(postfix_eval("5.1 8 -"), -2.9)
        with self.assertRaises(ValueError):
            postfix_eval("9 0 /")


    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")
    
    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 6 / 5 2 - / 8 5 1"),"6 5 2 / - 8 5 / 1 - *")
        self.assertEqual(prefix_to_postfix("+ 3 6"),"3 6 +")
        self.assertEqual(prefix_to_postfix("- 6 10"),"6 10 -")

if __name__ == "__main__":
    unittest.main()
