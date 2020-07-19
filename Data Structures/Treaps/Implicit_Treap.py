# https://cp-algorithms.com/data_structures/treap.html
# https://cp-algorithms.com/data_structures/treap.html
# https://ktshen.me/2016/05/29/Implicit%20Treap/
#https://sudonull.com/post/170748-Cartesian-tree-Part-3-Cartesian-tree-by-implicit-key

from random import randint


class TreapNode(object):

    def __init__(self,key, val,priority):
        self.key = key
        self.val = val
        self.priority = priority
        self.left = None
        self.right = None
        self.size = 1


class Treap(object):

    @staticmethod
    def gen():
        return randint(1, 2 ** 64)

    def __init__(self):
        self.root = None
        self.order = []

    def split(self,root,key):
        if root == None:
            return (None,None)
        curr_key= self.sz(root.left) + 1
        if curr_key <= key:
            root.right , right = self.split(root.right , key-curr_key)
            left = root
            self.update_sz(root)
            return (left, right)
        else:
            left, root.left = self.split(root.left, key)
            right = root
            self.update_sz(root)
        # self.update_height(root)
            return (left, right)

    def merge(self, left, right):
        if left == None:
            return right
        if right == None:
            return left
        if left.priority > right.priority:
            left.right = self.merge(left.right, right)
            root=left
        else:
            right.left = self.merge(left, right.left)
            root=right
        self.update_sz(root)
        self.root = root
        return self.root

    def find(self, t, key):
        if t == None:
            return False
        if t.key == key:
            return True
        elif key < t.key:
            return self.find(t.left, key)
        else:
            return self.find(t.right, key)

    def insert(self,key,val):
        node = TreapNode(key,val,self.gen())

        left, right = self.split(self.root,key)
        self.root = self.merge(left, node)
        self.root = self.merge(self.root, right)
        return self.root



    def sz(self, t):
        if t == None:
            return 0
        #ans = 1
        #ans = max(ans, self.get_height(t.left) + 1)
        #ans = max(ans, self.get_height(t.right) + 1)
        #ans = max(self.get_height(t.left),self.get_height(t.right)) + 1
        return t.size

    def update_sz(self,t):
        if t:
            t.size = self.sz(t.left) + 1 + self.sz(t.right)
        else:
             t.size = 1

    def inOrder(self, root,order=None):
        if order is None:
            self.order = []
        if not root:
            return

        self.inOrder(root.left, self.order)
        #print("{0} ".format(root.val), end="")
        self.order.append(root.val)
        self.inOrder(root.right, self.order)
        return self.order

    
#N,M=map(int,input().split())
#A=list(map(int,input().split()))
#Q=[list(map(int,input().split())) for i in range(M)]

N,M=8,4
A=[1,2,3,4,5,6,7,8]
# Q=[[1,2,4]]
Q=[[1,2,4],
 [2,3,5],
 [1,4,7],
 [2,1,4]]

#p = 100
mytreap = Treap()
root=None
for key,val in enumerate(A):
    mytreap.insert(key,val)
    #p -= 10
print(mytreap.inOrder(mytreap.root))


for q in Q:

    print(q)
    L, mid = mytreap.split(mytreap.root, q[1]-1)
    M, R = mytreap.split(mid, q[2]-q[1]+1)
    if q[0] == 1:
        print(mytreap.inOrder(L), mytreap.inOrder(M), mytreap.inOrder(R))
        LR = mytreap.merge(L, R)
        #print(mytreap.inOrder(LR))
        MLR = mytreap.merge(M, LR)
        print(mytreap.inOrder(MLR))

    else:
        print(mytreap.inOrder(L), mytreap.inOrder(M), mytreap.inOrder(R))
        RM = mytreap.merge(R, M)
        #print(mytreap.inOrder(LR))
        LRM = mytreap.merge(L,RM)
        print(mytreap.inOrder(LRM))

arr=mytreap.inOrder(mytreap.root)
F, mid = mytreap.split(mytreap.root, 1)
M, L = mytreap.split(mid, int(len(mytreap.inOrder(mid))-1))

NF=mytreap.inOrder(F)
NL=mytreap.inOrder(L)
print(NF, NL)
print(abs(int(NF)-int(NL)))
print(*arr)


# L,R=mytreap.split(mytreap.root,1)
#
# #for t in mytreap.split(mytreap.root, 1):
# print(mytreap.inOrder(L))
# M,R=mytreap.split(mytreap.root,4)
# print(mytreap.inOrder(M))
# print(mytreap.inOrder(R))
#
# #print(mytreap.inOrder(L) + mytreap.inOrder(R)+ mytreap.inOrder(M))
# N=mytreap.merge(L,R)
# print(mytreap.inOrder(N))
# O=mytreap.merge(M,N)
# print(mytreap.inOrder(O))
#
# L,R=mytreap.split(mytreap.root,3)
#
# #for t in mytreap.split(mytreap.root, 1):
# print(mytreap.inOrder(L))
# M,R=mytreap.split(mytreap.root,5)
# print(mytreap.inOrder(M))
# print(mytreap.inOrder(R))
