'''
A Python Implementation of Singly Linked Lists.
Functions include insertion/deletion to, searching and displaying the Linked List.
'''


# Creating a class for a Node which has the value and the location to the next value
class Node(object):
	def __init__(self,value):
		self.value = value
		self.next = None

	def getVal(self):
		return(self.value)

	def getNextVal(self):
		return(self.next)

	def setNextValue(self, nextVal):
		self.next = nextVal


# Creating a class for Linked List where the operations on the list are defined
class LinkedList(object):
	def __init__(self, head = None):
		self.head = head

	# Inserting a node at the head of the list and pointing this new to node to the head of the list	
	def insert(self, value):
		newNode = Node(value)
		newNode.setNextValue(self.head)
		self.head = newNode

	# Inserting at a specific index
	def insertAt(self, index, value):
		if index == 1:
			self.insert(value)

		current = self.head
		i = 1
		while i < index-1 and current is not None:
			current = self.head
			i = i + 1
		if current is None:
			raise IndexError('Index out of range!')
		else:
			newNode = Node(value)
			newNode.next = current.next
			current.next = newNode

	# Deleting a node with a specific value
	def delete(self, value):
		current = self.head
		previous = None
		found = False
		while current and found is False:
			if current.getVal() == value:
				found = True
			else:
				previous = current
				current = current.getNextVal()
		if current is None:
			raise ValueError('Data not in list')
		if previous is None:
			self.head = current.getNextVal()
		else:
			previous.setNextValue(current.getNextVal())

	# To query the size of the linked list
	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.getNextVal()
		return count

	# To search the linked list for a specific value
	def search(self, value):
		current = self.head
		found = False
		while current and found == False:
			if current.getVal() == value:
				found = True
			else:
				current = current.getNextVal()
		if current is None:
			raise ValueError('Element not in list')
		return found

	# To Display the linked list
	def display(self):
		current = self.head
		while current is not None:
			print(current.value)
			current = current.getNextVal()
		

newList = LinkedList()
newList.insert(1)
newList.insert(2)
newList.insert(4)
newList.insert(6)
newList.insertAt(2,5)
newList.display()
newList.delete(4)
print(newList.search(2))
newList.display()
