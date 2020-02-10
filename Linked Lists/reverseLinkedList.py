from singlyLinkedList import Node, LinkedList
def reverseIterative(self):
	prev = None
	curr = self.head
	while curr:
		nxt = curr.next
		curr.next = prev
		prev = curr
		curr = nxt
	self.head = prev

def reverseRecursive(self):
	def reverse(curr, prev):	
		if not curr:
			return prev
		nxt = curr.next
		curr.next = prev
		prev = curr
		curr = nxt
		return reverse(curr, prev)
	self.head = reverse(curr=self.head, prev=None)

LinkedList.reverseIterative = reverseIterative
LinkedList.reverseRecursive = reverseRecursive
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.reverseIterative()
print(llist.show())
llist.reverseRecursive()
print(llist.show())
