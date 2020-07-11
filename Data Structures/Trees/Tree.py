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
        self.height = 0

    def create(self, val):

        if self.root == None:
            self.root = Node(val)
            self.root.level = 0
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        current.left.level = current.level + 1

                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        current.right.level = current.level + 1
                        break
                else:
                    break




    def pre_order(self,root):
        print(' ' * 3 * root.level + '|__' +  str(root.info) )
        if root.left:
            self.pre_order(root.left)
        if root.right:
            self.pre_order(root.right)

    def in_order(self,root):
        print(root.info)
        if root.left:
            self.in_order(root.left)
        if root.right:
            self.in_order(root.right)

    def post_order(self,root):
        if root.left:
            self.post_order(root.left)
        if root.right:
            self.post_order(root.right)
        print(root.info)

    def height_tree(self,root):
        if root.level > self.height:
            self.height = root.level
        if root.left:
            self.height_tree(root.left)
        if root.right:
            self.height_tree(root.right)




def pre_order(root):
    tree.pre_order(root)

def height(root):
    tree.height_tree(root)
    print(tree.height)



tree = BinarySearchTree()
tree2 = BinarySearchTree()
arr = [3,2,1,5,4,6,7]
arr2 = [1,2,4,7,3,9,10,2,1]

for i in arr:
    tree.create(i)

for i in arr2:
    tree2.create(i)

pre_order(tree.root)
height(tree.root)
#pre_order(tree2.root)
