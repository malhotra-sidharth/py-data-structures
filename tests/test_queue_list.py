from data_structures.queue.queueList import QueueList
import unittest

class TestQueueList(unittest.TestCase):
  """
  Unit Tests for Queue Data Structure
  """

  def test_enqueue(self):
    """
    Test for enqueue method
    """
    queue = QueueList()
    self.assertEqual(queue.size(), 0)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    self.assertEqual(queue.size(), 3)

  def test_dequeue(self):
    """
    Test for dequeue method
    """
    queue = QueueList()
    self.assertEqual(queue.dequeue(), None)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    self.assertEqual(queue.dequeue(), 1)
    self.assertEqual(queue.size(), 2)

  def test_peek(self):
    """
    Test for peek method
    """
    queue = QueueList()
    self.assertEqual(queue.peek(), None)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    self.assertEqual(queue.peek(), 1)
    self.assertEqual(queue.size(), 3)

  def test_is_empty(self):
    """
    Test for is_empty method
    """
    queue = QueueList()
    self.assertEqual(queue.is_empty(), True)
    queue.enqueue(1)
    self.assertEqual(queue.is_empty(), False)

  def test_size(self):
    """
    Test for size method
    """
    queue = QueueList()
    self.assertEqual(queue.size(), 0)
    queue.enqueue(1)
    self.assertEqual(queue.size(), 1)


if __name__ == '__main__':
   unittest.main()
