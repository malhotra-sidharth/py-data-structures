from data_structures.stack import Stack
import unittest

class TestStack(unittest.TestCase):
  """
  Test the stack definition for data structures
  """

  def test_push(self):
    """
    Test for push method
    """
    stack = Stack()
    self.assertEqual(stack.size(), 0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    self.assertEqual(stack.size(), 3)


  def test_peek(self):
    """
    Test for peek method
    """
    stack = Stack()
    self.assertEqual(stack.peek(), None)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    self.assertEqual(stack.peek(), 3)
    self.assertEqual(stack.size(), 3)


  def test_pop(self):
    """
    Test for pop method
    """
    stack = Stack()
    self.assertEqual(stack.pop(), None)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    self.assertEqual(stack.pop(), 3)
    self.assertEqual(stack.size(), 2)


  def test_is_empty(self):
    """
    Test for is_empty method
    """
    stack = Stack()
    self.assertEqual(stack.is_empty(), True)
    stack.push(1)
    self.assertEqual(stack.is_empty(), False)
    stack.pop()
    self.assertEqual(stack.is_empty(), True)

  def test_size(self):
    """
    Test for size method
    """
    stack = Stack()
    self.assertEqual(stack.size(), 0)
    stack.push(1)
    self.assertEqual(stack.size(), 1)


if __name__ == '__main__':
  unittest.main()
