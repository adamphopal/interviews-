from collections import deque
stack = deque()


s = []
s.append('https://www.cnn.com/')
s.append('https://www.cnn.com/world')
s.append('https://www.cnn.com/india')
s.append('https://www.cnn.com/china')

print(s)

print(s[-1])
print(s.pop())

print(s)


#Implement Stack class using a deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)


s = Stack()
s.push(5) #adding
print(s.is_empty())
s.pop()             #removing
print(s.is_empty())


s.push(9)
s.push(34)
s.push(78)
s.push(12)

print(s.peek())  #getting the last item in the stack, last one is first one out
s.pop()
s.pop()
s.pop()
s.pop()
