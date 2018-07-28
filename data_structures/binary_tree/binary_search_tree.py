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


  def find(self, data):
    return self.__find(self.__root, data)


  def get_size(self):
    return self.__size

  def get_root(self):
    return self.__root


  def __find(self, node, data):
    if (node.get_data() == data):
      return True
    elif (node.is_leaf()):
      return False
    elif (data > node.get_data()):
      return self.__find(node.get_right_child(), data)
    else:
      return self.__find(node.get_left_child(), data)


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