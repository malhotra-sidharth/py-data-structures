from data_structures.binary_tree.binary_search_tree import BinarySearchTree
import unittest

class TestBinarySearchTree(unittest.TestCase):

  def test_insert(self):
    bst = BinarySearchTree()
    self.assertEqual(bst.get_size(), 0)
    bst.insert(4)
    bst.insert(3)
    bst.insert(5)
    self.assertEqual(bst.get_size(), 3)
    self.assertEqual(bst.get_root().get_data(), 4)
    self.assertEqual(bst.get_root().get_left_child().get_data(), 3)
    self.assertEqual(bst.get_root().get_right_child().get_data(), 5)


  def test_find(self):
    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(3)
    bst.insert(2)
    bst.insert(1)
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    self.assertEqual(bst.find(1), True)
    self.assertEqual(bst.find(7), True)
    self.assertEqual(bst.find(8), False)
    self.assertEqual(bst.find(0), False)


  def test_preorder(self):
    bst = BinarySearchTree()
    preorder = [4, 3, 2, 1, 5, 6, 7]
    bst.insert(4)
    bst.insert(3)
    bst.insert(2)
    bst.insert(1)
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    self.assertEqual(self.compare(bst.preorder(), preorder), True)


  def test_inorder(self):
    bst = BinarySearchTree()
    inorder = [1, 2, 3, 4, 5, 6, 7]
    bst.insert(4)
    bst.insert(3)
    bst.insert(2)
    bst.insert(1)
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    self.assertEqual(self.compare(bst.inorder(), inorder), True)


  def test_postorder(self):
    bst = BinarySearchTree()
    postorder = [1, 2, 3, 7, 6, 5, 4]
    bst.insert(4)
    bst.insert(3)
    bst.insert(2)
    bst.insert(1)
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    self.assertEqual(self.compare(bst.postorder(), postorder), True)

  def compare(self, lst1, lst2):
    for l1, l2 in zip(lst1, lst2):
      if l1 != l2:
        return False

    return True

if __name__ == '__main__':
    unittest.main()