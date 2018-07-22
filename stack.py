class Stack:
  '''
  Stack Data-structure
  '''

  def __init__(self):
    '''
    Initialize Stack list
    '''
    self.__stack = []


  def push(self, item):
    '''
    Appends item to the stack

    :param item: element to be added in stack
    '''
    self.__stack.append(item)


  def pop(self):
    '''
    Gives the most recent pushed element and removes it from the stack

    :return: most recent pushed item into the stack
    '''
    if len(self.__stack) == 0:
      return None
    else:
      item = self.__stack[-1]
      del self.__stack[-1]
      return item


  def peek(self):
    '''
     Looks at the most recent pushed element without removing it

    :return: the most recent saved element in the stack
    '''
    if len(self.__stack) == 0:
      return None
    else:
      return self.__stack[-1]


  def is_empty(self):
    '''
    Checks if the stack is empty or not

    :return: returns true if stack is empty else false
    '''
    return len(self.__stack) == 0


  def size(self):
    '''
    The size of the stack

    :return: returns unsigned integer for the count of values in the stack
    '''
    return len(self.__stack)


