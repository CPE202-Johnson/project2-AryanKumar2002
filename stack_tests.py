import unittest

from stack_array import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)

    #Tests for if size, push, pop, peak, is_empty, and is_full all work
    def test_complex(self):
        stack = Stack(3)
        self.assertTrue(stack.is_empty())
        stack.push(2)
        stack.push(4)
        stack.push(6)
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.size(), 3)
        stack.pop()
        stack.pop()
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.size(), 1)
    
    #Tests for if the errors are called when appropriate
    def test_error (self):
        stack = Stack(1)
        with self.assertRaises(IndexError):
            stack.peek()
        with self.assertRaises(IndexError):
            stack.pop()
        stack.push(1)
        with self.assertRaises(IndexError):
            stack.push(2)


if __name__ == '__main__': 
    unittest.main()
