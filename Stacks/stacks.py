'''
  A Python implementation of Stacks using classes and
  restricting the operations performed on the stack
  to just two, Push/Pop.
'''
class Stack:

  def __init__(self):
    self.stack = []

  def push(self, element):
    return self.stack.append(element)

  def pop(self):
    if len(self.stack) < 1:
      return None
    else:
      return self.stack.pop()

  def size(self):
    return len(self.stack)
    
  def isEmpty(self):
    return self.stack == []

  def stackTop(self):
    if not self.isEmpty():
      return self.stack[-1]

  def show(self):
    return self.stack

# Creating a new object of the class
newStack = Stack()
# Using the push() method from the class to add elements into Stack
newStack.push(1)
newStack.push(2)
newStack.push(3)
newStack.push(4)
newStack.push(5)
# Displaying the Stack using the show() method from the class
print("The Initial Stack: ", newStack.show())
# Using the size() method from the classs to fetch the stack size
print("The Size of the Stack: ", newStack.size())
# Using the pop() method to delete elements from the stack in FIFO manner
newStack.pop()
newStack.pop()
newStack.pop()
print("The Final Stack: ", newStack.show())
print("The Size of the Stack: ", newStack.size())
print("The top of the Stack is: ", newStack.stackTop())