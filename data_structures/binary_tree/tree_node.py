class TreeNode:

  def __init__(self, data, left_child=None, right_child=None, parent=None):
    self.__data = data
    self.__left = left_child
    self.__right = right_child
    self.__parent = parent


  def get_right_child(self):
    return self.__right


  def set_right_child(self, node):
    self.__right = node


  def get_left_child(self):
    return self.__left


  def set_left_child(self, node):
    self.__left = node


  def get_parent(self):
    return self.__parent


  def set_parent(self, node):
    self.__parent = node


  def get_data(self):
    return self.__data


  def set_data(self, data):
    self.__data = data


  def is_root(self):
    return self.__parent == None


  def is_leaf(self):
    return (self.__left == None and self.__right == None)


  def is_left_child(self):
    return (self.__parent != None and self.__parent.get_left_child() == self)


  def is_right_child(self):
    return (self.__parent != None and self.__parent.get_right_child() == self)


  def has_left_child(self):
    return self.get_left_child() != None


  def has_right_child(self):
    return self.get_right_child() != None
