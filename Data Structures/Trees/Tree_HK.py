from collections import deque,defaultdict,OrderedDict

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def create(self, val):

        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)

                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


    def get_level(self,node,data,level=0):
         if node is None:
             return 0
         if data == node:
             return level

         left_level = self.get_level(node.left,data,level+1)
         if left_level != 0: return left_level
         right_level = self.get_level(node.right,data,level+1)
         return right_level

    def pre_order(self,root,level=0,place="center"):
        print(' ' * self.get_level(self.root,root) * 3 + ("   " if root.info == self.root.info else "|__") +  str(root.info) )
        #print(root.info , end=' ')
        #if place == "left": print(str(root.info).ljust(self.get_level(self.root,root) * 3,"-"))
        #if place == "right": print(str(root.info).rjust(self.get_level(self.root, root) * 3, "-"))
        #if place == "center": print(str(root.info).center(self.get_level(self.root, root) * 3, " "))
        if root.left:
            self.pre_order(root.left,"left")
        if root.right:
            self.pre_order(root.right,"right")

    def in_order(self,root):

        if root.left:
            self.in_order(root.left)
        print(root.info, end=' ')
        if root.right:
            self.in_order(root.right)

    def post_order(self,root):
        if root.left:
            self.post_order(root.left)
        if root.right:
            self.post_order(root.right)
        print(root.info)


#def pre_order(root):
#    tree.pre_order(root)


def height_tree(node):
    if node is None:
        return 0;

    else:

        lDepth = height_tree(node.left)
        rDepth = height_tree(node.right)

        # Use the larger one
        if (lDepth > rDepth):
            return lDepth + 1
        else:
            return rDepth + 1

def level_traversal(node):
    q = deque()
    while node:
        print(node.info)
        if node.left: q.appendleft(node.left)
        if node.right: q.appendleft(node.right)
        try:
            node = q.pop()
        except:
            node = None

def getVerticalOrder(node,m,hd):
    if node:
        m[hd].append(node.info)
        getVerticalOrder(node.left,m,hd-1)
        getVerticalOrder(node.right,m,hd+1)

def top_view(node):
    m=defaultdict(list)
    hd=0
    getVerticalOrder(node,m,hd)
    print(sorted(m.items()))

    for i in sorted(m):
        print(m[i][0], end=' ')

def top_view_level_traversal(node):
    q=deque()
    m=defaultdict(list)
    hd_node=defaultdict(list)

    q.appendleft(node)
    hd_node[node] = 0
    m[0].append(node.info)

    while q:
        temp = q.pop()
        if temp.left:
            q.appendleft(temp.left)
            hd_node[temp.left] = hd_node[temp] - 1
            m[hd_node[temp] - 1].append(temp.left.info)

        if temp.right:
            q.appendleft(temp.right)
            hd_node[temp.right] = hd_node[temp] + 1
            m[hd_node[temp] + 1].append(temp.right.info)

    sorted_m = OrderedDict(sorted(m.items()))
    for i in sorted_m:
        print(m[i][0], end=' ')

def least_common_ancestor(node,v1,v2):
    if node is None:
        return
    while node:
        if (v1 < node.info and v2 < node.info):
            node = node.left
        elif (v1 > node.info and v2 > node.info):
            node = node.right
        else:
            print(node.info)
            break


def decodeHuff(root, s):  #s="1001011"
    decode = ""
    for bit in s:
        if bit == 0:
            root = root.left
        else:
            root = root.right

        if not root.left and not root.right:
            decode += root.data
    print(decode)


## main program
tree = BinarySearchTree()
tree4 = BinarySearchTree()
arr = [1,2,5,3,4,6]
arr2 = [1,2,4,7,3,9,10,2,1]
arr3 = [37,23,108,59,86,64,94,14,105,17,111,65,55,31,79,97,78,25,50,22,66,46,104,98,81,90,68,40,103,77,74,18,69,82,41,4,48,83,67,6,2,95,54,100,99,84,34,88,27,72,32,62,9,56,109,115,33,15,91,29,85,114,112,20,26,30,93,96,87,42,38,60,7,73,35,12,10,57,80,13,52,44,16,70,8,39,107,106,63,24,92,45,75,116,5,61,49,101,71,11,53,43,102,110,1,58,36,28,76,47,113,21,89,51,19,3]
arr4 = [8,4,9,1,2,3,6,5]
# for i in arr:
#      tree.create(i)
#
# for i in arr2:
#     tree2.create(i)

for i in arr4:
    tree4.create(i)

tree4.pre_order(tree4.root)
#tree3.in_order(tree3.root)
#print(height_tree(tree.root))
#level_traversal(tree.root)
#top_view(tree3.root)
#top_view_level_traversal(tree3.root)
least_common_ancestor(tree4.root,1,2)
