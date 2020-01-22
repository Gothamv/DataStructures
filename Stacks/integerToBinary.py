from stacks import Stack
def integerToBinary(num: int) -> str:
  #Initialising the Stack Object
	s = Stack()
	ans = num
	while ans != 0:
    #Appending the remainder to the Stack
		s.push(ans % 2)
    #Storing the non decimal part of divison by floor divison
		ans = ans//2 
	binary = ""
  #While stack isn't empty pop into binary
	while not s.isEmpty():
		binary += str(s.pop())
	return binary

#Driver Code
print(integerToBinary(42069))
