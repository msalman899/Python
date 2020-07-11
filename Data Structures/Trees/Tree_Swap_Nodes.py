from collections import deque, defaultdict, OrderedDict
sys.setrecursionlimit(15000)

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
        self.root = Node(1)
        self.order = []

    def search_node(self,root,node):
        if root is None:
            return 0
        if root.info == node:
            return root
        left_search = self.search_node(root.left,node)
        if left_search != 0: return left_search
        right_search = self.search_node(root.right,node)
        return right_search


    def create(self, node, left, right):
        current = self.search_node(self.root,node)
        if left != -1: current.left = Node(left)
        if right != -1: current.right = Node(right)

    def swap(self,root,node):
        node_swap = self.search_node(root, node)
        node_swap.left, node_swap.right = node_swap.right, node_swap.left

    def in_order(self,root):
        if root == self.root:
            self.order=[]
        if root.left:
            self.in_order(root.left)
        self.order.append(root.info)
        if root.right:
            self.in_order(root.right)
        return self.order

def level_traversal(node):
    q = deque()
    m = defaultdict(list)
    node.level = 1
    while node:
        m[node.level].append(node.info)
        if node.left:
            q.appendleft(node.left)
            node.left.level = node.level + 1
        if node.right:
            q.appendleft(node.right)
            node.right.level = node.level + 1

        try:
            node = q.pop()
        except:
            node = None
    return m


def swapNodes(indexes, queries):
    tree = BinarySearchTree()
    swap_final=[]
    for i in range(len(indexes)):
        tree.create(i+1, indexes[i][0],indexes[i][1])

    level_node = level_traversal(tree.root)
    for k in queries:
        print(level_node)
        mul=1
        while level_node[k*mul]:
            for i in level_node[k*mul]:
                #print(i)
                tree.swap(tree.root,i)
                #print(tree.in_order(tree.root))
                #print(swap_final)
            mul += 1
        swap_final.append(tree.in_order(tree.root))
    return swap_final


indexes = [[2,3],[-1,-1],[-1,-1]]
queries = [1,1]
#indexes = [[2,3],[4,-1],[5,-1],[6,-1],[7,8],[-1,9],[-1,-1],[10,11],[-1,-1],[-1,-1],[-1,-1]]
#queries = [2,4]
result = swapNodes(indexes, queries)
print(result)
