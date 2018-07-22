from blist import blist

class Queue:
  """
  Queue Data-structure
  FIFO
  """
  def __init__(self):
    """
    Initialize a queue list
    """
    self.__queue = blist()


  def enqueue(self, item):
    """
    Adds item to the queue
    complexity: O(log N)

    :param item: item to be added to the queue
    """
    self.__queue.append(item)


  def dequeue(self):
    """
    Removes the oldest element from the queue
    complexity: O(log N)

    :return: The oldest element from the queue
    """
    if len(self.__queue) == 0:
      return None
    else:
      item = self.__queue[0]
      del self.__queue[0]
      return item


  def peek(self):
    """
    Gets the oldest element from the queue withour removing it
    complexity: O(1)

    :return: The oldest element from the queue
    """
    if len(self.__queue) == 0:
      return None
    else:
      return self.__queue[0]


  def size(self):
    """
    Size of the queue
    complexity: O(1)

    :return: unsigned integer denoting count of elements in the queue
    """
    return len(self.__queue)


  def is_empty(self):
    """
    Checks if queue is empty or not
    complexity: O(1)

    :return: True if queue is empty else Flase
    """
    return len(self.__queue) == 0
