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

	def deleteByValue(self, key):
		curr = self.head
		# Node to be deleted is a head
		if curr and curr.data == key:
			self.head = curr.next
			curr = None
			return
		
		#Node to be deleted is not a head
		prev = None
		while curr and curr.data != key:
			prev = curr
			curr = curr.next
		
		#Checking if thw while loop terminated because of None and not because of key matching
		if curr is None:
			return
		prev.next = curr.next
		curr = None

	def deleteByPosition(self, pos):
		if self.head:
			curr = self.head
			if pos == 0:
				self.head = curr.next
				curr = None
				return
		
		prev = None
		count = 0
		if curr and count != pos:
			prev = curr
			curr = curr.next
			count += 1

		if curr is None:
			return
		
		prev.next = curr.next
		curr = None
		return

	def show(self) -> list:
		showList = []
		currNode = self.head
		while currNode:
			showList.append(currNode.data)
			currNode = currNode.next	
		return showList

	def lenIterative(self) -> int:
		count = 0
		curr = self.head
		while curr:
			count +=1
			curr = curr.next
		return count

	def lenRecursive(self, node):
		if node is None:
			return 0
		return 1 + self.lenRecursive(node.next)

''' Driver Code
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.deleteByValue("B")
llist.deleteByPosition(0)
print(llist.show())
'''
