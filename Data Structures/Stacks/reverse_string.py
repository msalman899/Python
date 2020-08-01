from _collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def top(self):
        if self.is_empty():
            return (0,0)
        return self.container[-1]

    def is_empty(self):
        return True if len(self.container) == 0 else False

    def size(self):
        return len(self.container)

    def max(self):
        return self.top()[1]

# write a function to reverse string "Python Program"
str="Python Program"
s = Stack()
for char in str:
    s.push(char)

for _ in range(len(str)):
    print(s.pop(), end="")
    
outout --> margorP nohtyP
