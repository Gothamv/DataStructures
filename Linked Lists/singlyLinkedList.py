class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def append(self, data):
		newNode = Node(data)
		if self.head is None:
			self.head = newNode
			return
		lastNode = self.head
		while lastNode.next:
			lastNode = lastNode.next
		lastNode.next = newNode
	
	def prepend(self,data):
		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode

	def insertAfter(self, prevNode, data):
		if not prevNode:
			print('The node does not exist in the list!')
		newNode = Node(data)
		newNode.next = prevNode.next
		prevNode.next = newNode 

	def show(self) -> list:
		showList = []
		currNode = self.head
		while currNode:
			showList.append(currNode.data)
			currNode = currNode.next	
		return showList
	
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
print(llist.show())



