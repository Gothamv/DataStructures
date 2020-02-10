from singlyLinkedList import Node, LinkedList

def mergeSortedLinkedList(self, llist):
	p = self.head
	q = llist.head
	s = None #Points to smaller of the two heads of the respective linked list

	# If p is empty return the already sorted q as it is and vice versa
	if not p:
		return q
	if not q:
		return p
	
	# Assignment of s which is the new head
	if p and q:
		if p.data <=q.data:
			s = p
			p = s.next
		else:
			s = q
			q = s.next
		newHead = s
	
	#Iterating through the 2 lists
	while p and q:
		if p.data <= q.data:
			s.next = p
			s = p
			p = s.next
		else:
			s.next = q
			s = q
			q = s.next
	# Checking if we have reached the end of the lists
	if not p:
		s.next = q
	if not q:
		s.next = p
	return newHead

LinkedList.mergeSortedLinkedList = mergeSortedLinkedList
llist1 = LinkedList()
llist2 = LinkedList()
llist1.append(1)
llist1.append(5)
llist1.append(7)
llist1.append(9)
llist1.append(10)
llist2.append(2)
llist2.append(3)
llist2.append(4)
llist2.append(6)
llist2.append(8)
llist1.mergeSortedLinkedList(llist2)
print(llist1.show())