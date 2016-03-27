#!/usr/bin/env python

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
        if self.isEmpty():
        	return ('StackUnderflow')
        else:
         	return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

s=Stack()

print(s.isEmpty())

s.push('Shivang')
s.push('Shaifali')
print('The top element right now in stack is: '+ s.peek())
s.push('Madhu')
s.push('Ashok')
print(s.pop())
print(s.size())
print(s.pop())
print(s.size())
print(s.pop())
print(s.size())
print(s.pop())
print(s.size())
print(s.pop())