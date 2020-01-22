#Importing Class Stack from stacks.py
from stacks import Stack
def stringReverse(s: str) -> str:
	#Creating a Stack Object
	stack = Stack()
	#For every character in string push to stack
	for x in s:
		stack.push(x)
	revStr = "" #The string to be returned
	#While the stack is not empty
	while not stack.isEmpty():
		#Add the popped element to the revStr
		revStr += stack.pop()
	return revStr

#Driver Code
s = 'Hello'
print(stringReverse(s))
