from singlyLinkedList import Node, LinkedList
def nodeSwap(self, key1, key2):
	if key1 == key2:
		return
	
	prev1 = None
	curr1 = self.head
	while curr1 and curr1.data != key1:
		prev1 = curr1
		curr1 = curr1.next
	
	prev2 = None
	curr2 = self.head
	while curr2 and curr2.data != key2:
		prev2 = curr2
		curr2 = curr2.next
		
	# If keys do not exist
	if not curr1 or not curr2:
		return
	
	if prev1:
		prev1.next = curr2
	else:
		self.head = curr2
	
	if prev2:
		prev2.next = curr1
	else:
		self.head = curr1
	
	curr1.next, curr2.next = curr2.next, curr1.next

LinkedList.nodeSwap = nodeSwap
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.nodeSwap("A","B")
print(llist.show())
