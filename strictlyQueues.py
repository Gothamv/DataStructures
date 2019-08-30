'''
A Python implementation of Queues using classes and
restricting the operations performed on the queue to
just two, enqueue/dequeue.
'''

class Queue:

	def __init__(self):
		self.queue = []

	def push(self, element):
		return self.queue.append(element)

	def pop(self):
		if len(self.queue) < 1:
			return None
		else:
			return self.queue.pop(0)

	def size(self):
		return len(self.queue)

	def show(self):
		return self.queue

# Creating a new object of the class
newQueue = Queue()
# Using the push() method from the class to add elements into Queue
newQueue.push(1)
newQueue.push(2)
newQueue.push(3)
newQueue.push(4)
newQueue.push(5)
# Using the size() method from the classs to fetch the Queue size
print("The Size of the Queue: ", newQueue.size())
# Displaying the Queue using the show() method from the class
print("The Initial Queue: ", newQueue.show())
# Using the pop() method to delete elements from the Queue in LIFO manner
newQueue.pop()
newQueue.pop()
newQueue.pop()
print("The Final Queue: ", newQueue.show())
print("The Size of the Queue: ", newQueue.size())
