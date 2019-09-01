'''
A Python implementation of the Double Ended Queue or Deque.
Insertion and Deletion can be done at both ends of the queue.
'''

class Deque:

	def __init__(self):
		self.queue = []

	def size(self):
		#Return the size of the Queue
		return len(self.queue)

	def addToLeft(self,element):
		#Add the element to the left end of the Queue
		self.queue.insert(0,element)

	def addToRight(self,element):
		#Add the element to the right end of the Queue
		self.queue.append(element)

	def removeFromLeft(self):
		#Remove element from the left end of the Queue
		return self.queue.pop(0)

	def removeFromRight(self):
		#Remove element from the right end of the Queue
		return self.queue.pop()

	def show(self):
		#Display the Queue
		return self.queue

#Dequeue object
dq = Deque()
#Inserting to left & right end of the Queue
dq.addToLeft(1)
dq.addToRight(2)
dq.addToLeft(3)
dq.addToRight(4)
dq.addToLeft(5)
print('The initial Queue: ', dq.show())
print('The size of the Queue: ', dq.size())
#Removing from left & right end of the Queue
dq.removeFromLeft()
dq.removeFromRight()
dq.removeFromLeft()
dq.removeFromRight()
print('The final Queue: ', dq.show())
print('The size of the Queue: ', dq.size())
