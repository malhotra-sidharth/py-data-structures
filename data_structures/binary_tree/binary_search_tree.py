from data_structures.binary_tree.tree_node import TreeNode


class BinarySearchTree:

  def __init__(self):
    self.__root = None
    self.__size = 0


  def insert(self, data):
    node = TreeNode(data)
    self.__size += 1
    if (self.__root == None):
      self.__root = node
    else:
      self.__insert(self.__root, node)

  def get_size(self):
    return self.__size

  def get_root(self):
    return self.__root

  def preorder(self):
    lst = []
    self.__preorder(self.__root, lst)
    return lst

  def inorder(self):
    lst = []
    self.__inorder(self.__root, lst)
    return lst

  def postorder(self):
    lst = []
    self.__postorder(self.__root, lst)
    return lst

  def find(self, data):
    return self.__find(self.__root, data)

  def __find(self, node, data):
    if (node.get_data() == data):
      return True
    elif (node.is_leaf()):
      return False
    elif (data > node.get_data()):
      return self.__find(node.get_right_child(), data)
    else:
      return self.__find(node.get_left_child(), data)

  def __preorder(self, root, lst):
    if root != None:
      lst.append(root.get_data())
      self.__preorder(root.get_left_child(), lst)
      self.__preorder(root.get_right_child(), lst)

  def __inorder(self, root, lst):
    if root != None:
      self.__inorder(root.get_left_child(), lst)
      lst.append(root.get_data())
      self.__inorder(root.get_right_child(), lst)

  def __postorder(self, root, lst):
    if root != None:
      self.__postorder(root.get_left_child(), lst)
      self.__postorder(root.get_right_child(), lst)
      lst.append(root.get_data())

  def __insert(self, root, node, parent=None):
    if (node.get_data() > root.get_data()):
      if (root.has_right_child()):
        return self.__insert(root.get_right_child(), node, root)
      else:
        root.set_right_child(node)
        node.set_parent(root)
        return
    else:
      if (root.has_left_child()):
        return self.__insert(root.get_left_child(), node, root)
      else:
        root.set_left_child(node)
        node.set_parent(root)
        return

  # IN-PRE_POST ORDERS
  # TREE-MINIMUM-MAXIMUM
  # TREE SUCCESSOR