import abc

class Node(metaclass=abc.ABCMeta):
  """
  Interface for oneway node, two way node or any other node
  that will be used to build a linked list
  """
  @abc.abstractmethod
  def get_data(self):
    """
    Gets the data of this node

    :return: data of this node
    """
    pass


  @abc.abstractmethod
  def set_data(self, data):
    """
    Sets data for this node

    :param data: data for this node
    """
    pass


  @abc.abstractmethod
  def get_next(self):
    """
    Gets the pointer to the next node

    :return: pointer to the next node
    """
    pass


  @abc.abstractmethod
  def set_next(self, node):
    """
    Sets given node as next node pointer of this node

    :param node: node pointer to next node
    """
    pass
