'''
A Python implementation of the Priority Queues.
Elements are removed based on the priority no. associated with each element.
Incase of the same priority number, FIFO is used to break the tie.
Higher the number, higher priority is assumed.
'''

class Node:

	def __init__(self,element,priority):
		#Elmenet to be added
		self.element = element
		#Priority of the element
		self.priority = priority


class PriorityQ:

	def __init__(self):
		#Initalising the queue as a list
		self.queue = []

	def size(self):
		#Returning the size of the queue
		return len(self.queue)

	def enqueue(self, node):
		#Adding elements to the queue
		#Queue empty conditon
		if self.size() == 0:
			self.queue.append(node)
		#If Queue not empty
		else:
			#Traversing throught the queue to find a location for our element
			for i in range(0, self.size()):
				#If the prioity of the new node is higher than the nodes currently in the queue
				if node.priority >= self.queue[i].priority:
					#If we reached the end of queue
					if i == (self.size() - 1):
						#Inserting element at the end
						self.queue.insert(i+1, node)
					else:
						continue
				#If the priority of the new node is not the greatest
				else:
					self.queue.insert(i, node)
					return True

	def dequeue(self):
		#LIFO popping
		return self.queue.pop(0)

	def show(self):
		#Displaying the queue along with their priorities
		for i in self.queue:
			print(str(i.element)+" Priority: "+str(i.priority))



#PriorityQ object
pq = PriorityQ()
#Creating multiple node objects
node1 = Node('1', 3)
node2 = Node('2', 2)
node3 = Node('3', 1)
node4 = Node('4', 26)
node5 = Node('5', 25)
#Adding elements in the queue
pq.enqueue(node1)
pq.enqueue(node2)
pq.enqueue(node3)
pq.enqueue(node4)
pq.enqueue(node5)
print('The initial queue along with their priorities : ')
pq.show()
print('The size of the queue: ', pq.size())
print('\n')
#Removing elements from the queue
pq.dequeue()
print('The current queue along with their priorities : ')
pq.show()
print('The size of the queue: ', pq.size())
print('\n')
pq.dequeue()
print('The current queue along with their priorities : ')
pq.show()
print('The size of the queue: ', pq.size())
print('\n')
