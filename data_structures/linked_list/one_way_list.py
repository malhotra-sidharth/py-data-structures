from data_structures.linked_list.oneway_node import OneWayNode


class OneWayList:
  """
  Creates a linked list that can only be traversed in forward direction
  """

  def __init__(self):
    self.__head = None
    self.__size = 0


  def add(self, data):
    """
    Adds a new node to this list
    Complexity => O(1)

    :param data: data of the node to be added to this list
    """
    node = OneWayNode(data)
    node.set_next(self.__head)
    self.__head = node
    self.__size += 1


  def is_empty(self):
    """
    Checks if the list is empty or not
    Complexity => O(1)

    :return: True if list is empty else False
    """
    return self.__head == None


  def size(self):
    """
    Size of the list
    Complexity => O(1)

    :return: unsigned integer for size of the list
    """
    return self.__size


  def search(self, data):
    """
    Searched for the given data in this list
    Complexity => O(N)

    :param data: item to be searched
    :return: True if data is found in the list else False
    """
    start = self.__head
    found = False
    while start != None:
      if start.get_data() == data:
        found = True
        break
      else:
        start = start.get_next()

    return found


  def remove(self, data):
    """
    Removes the first occurence of the node with the given data from this list
    Complexity => O(N)

    :param data: data of the node which is to be removed
    :return: True if node is found and deleted else False
    """
    start = self.__head
    previous = None
    deleted = False
    while start != None:
      if start.get_data() == data:
        if previous == None:
          self.__head = start.get_next()
        else:
          previous.set_next(start.get_next())
        deleted = True
        self.__size -= 1
      else:
        previous = start
        start = start.get_next()

    return deleted

