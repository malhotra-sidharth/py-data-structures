from data_structures.linked_list.node import Node


class TwoWayNode(Node):
  """
  Node for creating two way linked list
  """

  def __init__(self, data):
    self.__data = data
    self.__next = None
    self.__previous = None


  def get_data(self):
    return self.__data


  def set_data(self, data):
    self.__data = data


  def get_next(self):
    return self.__data


  def set_next(self, node):
    self.__next = node


  def get_previous(self):
    return self.__previous


  def set_previous(self, node):
    self.__previous = node

