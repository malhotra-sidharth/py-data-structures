from data_structures.linked_list.one_way_list import OneWayList
import unittest

class TestOneWayList(unittest.TestCase):
  """
  Tests the definition of OneWayList
  """

  def test_add(self):
    """
    Test add method
    """
    lst = OneWayList()
    self.assertEqual(lst.size(), 0)
    lst.add(1)
    lst.add(2)
    lst.add(3)
    self.assertEqual(lst.size(), 3)


  def test_is_empty(self):
    """
    Test is_empty method
    """
    lst = OneWayList()
    self.assertEqual(lst.is_empty(), True)
    lst.add(1)
    self.assertEqual(lst.is_empty(), False)


  def test_size(self):
    """
     Test size method
    """
    lst = OneWayList()
    self.assertEqual(lst.size(), 0)
    lst.add(1)
    self.assertEqual(lst.size(), 1)


  def test_search(self):
    """
     Test search method
    """
    lst = OneWayList()
    lst.add(1)
    lst.add(2)
    lst.add(3)
    lst.add(4)
    lst.add(5)
    self.assertEqual(lst.search(3), True)
    self.assertEqual(lst.search(6), False)


  def test_remove(self):
    """
     Test remove method
    """
    lst = OneWayList()
    lst.add(1)
    lst.add(2)
    lst.add(3)
    lst.add(4)
    lst.add(5)
    self.assertEqual(lst.size(), 5)
    self.assertEqual(lst.remove(4), True)
    self.assertEqual(lst.size(), 4)
    self.assertEqual(lst.remove(6), False)
    self.assertEqual(lst.size(), 4)


if __name__ == '__main__':
    unittest.main()
