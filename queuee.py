#Implement queue class using collections.deque
from collections import deque
#q = deque()

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)


pq = Queue()

pq.enqueue({                        #adding
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({                        #adding
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({                        #adding
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

print(pq.buffer)
print(pq.size())
print(pq.dequeue()) #removing ques, first one in, is first one out 131.10
print(pq.dequeue()) #removing ques, first one in, is first one out 132
print(pq.buffer)
print(pq.size())
print(pq.dequeue()) #removing ques, first one in, is first one out 135
print(pq.size())
