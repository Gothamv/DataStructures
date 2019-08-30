'''
A Python implementation of Stacks using Python Lists.
'''

# Create a List to store the elements
stack = []
# Pushing elements into the list using the append() method
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
# Displaying the Stack Elements
print("The initial stack : ", stack) 
# Deleting the stack elements in FIFO manner
# Wraping the stack.pop() statemtn inside a print statement to see which element is being deleted
print("Deleting: ", stack.pop())
print("Deleting: ", stack.pop())
print("Deleting: ", stack.pop())
# Displaying the stack after deleting 3 elements of the list
print("The final stack after deletion: ", stack)
