'''
A Python implementation of Queues using deque.
'''

from collections import deque
# Initialising the Queue
queue = deque()
# Using the append() method to add elements into the Queue (enqueue)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
# Displaying the Queue
print('The Initial Queue: ', queue)
# Using the popleft() method to delete elements from the Queue (dequeue)
queue.popleft()
queue.popleft()
queue.popleft()
print('The Final Queue: ', queue)
