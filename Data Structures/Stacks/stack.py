from _collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val,max):
        self.container.append((val,max))

    def pop(self):
        self.container.pop()

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


-- Problem https://www.hackerrank.com/challenges/maximum-element/problem
n=int(input())
s = Stack()
for _ in range(n):
    type,*val = map(int,input().split())
    if type == 1:
        if val[0] > s.top()[1]:
            s.push(val[0],val[0])
        else:
            s.push(val[0], s.top()[1])
    elif type == 2:
        s.pop()
    else:
        print(s.max())
