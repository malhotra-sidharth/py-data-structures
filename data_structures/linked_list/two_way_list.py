from data_structures.linked_list.two_way_node import TwoWayNode


class TwoWayList:
  """
  Creates a linked list that can be traversed in both directions
  """

  def __init__(self):
    self.__head = None
    self.__size = 0


  def add(self, data):
    """
    Adds a new node to the list
    Complexity => O(1)

    :param data: data of the node to be inserted in the list
    """

    node = TwoWayNode(data)
    node.set_next(self.__head)
    self.__head = node
    self.__size += 1