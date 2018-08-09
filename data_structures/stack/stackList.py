from data_structures.linked_list.oneway_node import OneWayNode

class StackList:
  """
    Stack using OneWay Linked List
  """
  def __init__(self):
    self.__head = None
    self.__size = 0

  def push(self, data):
    """"
    Appends item to the stack
    complexity: O(1)

    :param item: element to be added in stack
    """
    node = OneWayNode(data)
    self.__head = node
    node.set_next(self.__head)
    self.__size += 1


  def peek(self):
    """
     Looks at the most recent pushed element without removing it
     complexity: O(1)

    :return: the most recent saved element in the stack
    """
    if self.__size == 0:
      return None
    else:
      return self.__head.get_data()


  def pop(self):
    """
    Gives the most recent pushed element and removes it from the stack
    complexity: O(1)

    :return: most recent pushed item into the stack
    """
    if self.__size == 0:
      return None
    else:
      data = self.__head.get_data()
      self.__head = self.__head.get_next()
      self.__size -= 1
      return data

  def size(self):
    """
    Size of the stack
    complexity: O(1)

    :return: unsigned integer denoting count of elements in the stack
    """
    return self.__size

  def is_empty(self):
    """
    Checks if stack is empty or not
    complexity: O(1)

    :return: True if stack is empty else Flase
    """
    return self.__size == 0

