from data_structures.linked_list.oneway_node import OneWayNode

class QueueList:
  """
    Queue using OneWay Linked List
  """
  def __init__(self):
    self.__head = None
    self.__next = None
    self.__size = 0

  def enqueue(self, data):
    """
    Adds new data value to the Queue
    Complexity -> O(1)

    :param data: data to be inserted in the queue
    """
    node = OneWayNode(data)
    if self.__size == 0:
      self.__head = node
      self.__next = node
    else:
      self.__next.set_next(node)
      self.__next = node
    self.__size += 1


  def peek(self):
    """
    Fetches the data of the  oldest element in teh Queue
    without removing that element form Queue
    Complexity: O(1)

    :return: The oldest element from teh queue
    """
    if self.__size == 0:
      return None
    else:
      return self.__head.get_data()


  def dequeue(self):
    """
    Removes the oldest element from the queue
    complexity: O(1)

    :return: The oldest element from the queue
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
    Size of the queue
    complexity: O(1)

    :return: unsigned integer denoting count of elements in the queue
    """
    return self.__size

  def is_empty(self):
    """
    Checks if queue is empty or not
    complexity: O(1)

    :return: True if queue is empty else Flase
    """
    return self.__size == 0

