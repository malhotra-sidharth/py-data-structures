from data_structures.linked_list.node import Node

class OneWayNode(Node):
  """
  Node for creating one way linked list
  """

  def __init__(self, data):
    self.__data = data
    self.__next = None


  def get_data(self):
    return self.__data


  def set_data(self, data):
    self.__data = data


  def get_next(self):
    return self.__next


  def set_next(self, node):
    self.__next = node
