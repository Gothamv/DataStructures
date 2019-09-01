'''
A Python implementaion of the Circular Queue.
'''

class CircularQueue:

	def __init__(self, max):
		self.queue = []
		self.max = max
		self.head = 0
		self.tail = 0

	def size(self):
		if self.tail >= self.head:
			cqSize = self.tail - self.head
		else:
			cqSize = self.max - (self.head - self.tail)
		return cqSize

	def enqueue(self, element):
		#Queue full condition
		if self.size() == (self.max - 1):
			return('Queue Full!')
		else:
			#Add the element to the queue
			self.queue.append(element)
			#Increment the tail
			self.tail = (self.tail+1) % self.max

	def dequeue(self):
		#Queue empty
		if self.size == 0:
			return('Queue is empty!')
		else:
			#Fetching the element to be dequeued for displaying
			element = self.queue[self.head]
			#Increment the head
			self.head = (self.head+1) % self.max
			return("Dequeued element: ",element)

	def show(self):
		cq = self.queue
		cqShow = []
		#For loop to iterate through queue and display only the 
		#elements currently present in the queue
		for _ in range(self.head, self.tail):
			cqShow.append(cq[_])
		return cqShow

#Circular Queue Object; Passing the max size as the parameter to the object
cq = CircularQueue(8)
#Adding elements to the queue
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
#Using the show() method to display the queue
print("The Initial Queue: ", cq.show())
#Using the size() method to fetch the size of the queue
print("The Size of the Queue: ", cq.size())
#Removing elements from the queue
cq.dequeue()
cq.dequeue()
cq.dequeue()
print("The Final Queue: ", cq.show())
print("The Size of the Queue: ", cq.size())
