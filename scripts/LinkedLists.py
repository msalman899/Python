class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self,start=None):
        self.start = start

    def display_list(self):
        link_list=[]
        if self.start:
            print("Displaying List:")
            n = self.start
            while n:
                link_list.append(n.data)
                n = n.next
            print(*link_list)
        else:
            print("List is empty")

    def insert_empty(self,data):
        print("**Adding node " + str(data) + " to empty list**")
        node = Node(data)
        self.start = node

    def insert_begining(self,data):
        if self.start is None:
            self.insert_empty(data)
            return
        print("**Adding node " + str(data) + " in the begining of list**")
        node = Node(data)
        node.next = self.start
        self.start = node


    def insert_end(self,data):
        if self.start is None:
            self.insert_empty(data)
            return
        n = self.start
        print("**Adding node " + str(data) + " in the end of list**")
        while n.next:
            n = n.next
        node = Node(data)
        n.next = node

    def search_node(self,data):
        if self.start:
            n = self.start
            k=1
            while n:
                if n.data == data:
                    print("Node " + str(n.data) + " is at position ", k)
                    return n
                n = n.next
                k += 1
            print("Node " + str(data) + " not found!!")
            return False
        print("Node " + str(data) + " not found!!")

    def insert_before_node(self,ref_node_data,data):
        if self.start:
            n = self.start
            while n.next:
                if n.next.data == ref_node_data:
                    node = Node(data)
                    node.next = n.next
                    n.next = node
                    return
                n = n.next
        print("Node " + str(data) + " not found!!")

    def insert_after_node(self,ref_node_data,data):
        ref_node = self.search_node(ref_node_data)
        if ref_node:
            node = Node(data)
            node.next = ref_node.next
            ref_node.next = node

    def insert_node_position(self,position,data):
        n,i = self.start,1
        while n and i < position-1:
            n = n.next
            i += 1
        if n:
            node = Node(data)
            node.next = n.next
            n.next = node
        else:
            print("Position ", position, "doesn't exist OR the List is empty")

    def delete_first_node(self):
        if self.start:
            if self.start.next is None:
                self.start = None
                return
            self.start = self.start.next
            return
        print("List is empty")

    def delete_only_node(self):
        self.delete_first_node()

    def delete_between_node(self,ref_node_data):
            n = self.start
            while n.next:
                if n.next.data == ref_node_data:
                    n.next = n.next.next
                    return
                n = n.next
            print("Node " + str(data) + " not found!!")

    def delete_last_node(self):
        n = self.start
        if n.next:
            while n.next.next:
                n = n.next
            n.next = None
            return
        self.delete_only_node()

def call_function(func):
    count = int(input("Enter the # of elements you want to add: "))
    i = 1
    while i <= count:
        data = int(input("Enter the element value: "))
        getattr(sll,func)(data)
        i += 1


selection=0
sll = SingleLinkedList()
while selection != 13:
    print("\n Select the option from below list: \n"
    "1 - Diplay the list \n"
    "2 - Insert node into beginning of the list\n"
    "3 - Insert node into end of the list\n"
    "4 - Search a node\n"
    "5 - Insertion before a node \n"
    "6 - Insertion after a node \n"
    "7 - Insertion in between the nodes \n"
    "8 - Insert node at a given position \n"
    "9 - Delete first node \n"
    "10 - Delete the only node \n"
    "11 - Delete in between the node \n"
    "12 - Delete the last node \n"
    "13 - Quit")

    selection = int(input("enter your choice: "))

    if selection == 1:
        sll.display_list()
    elif selection == 2:
        call_function("insert_begining")
    elif selection == 3:
        call_function("insert_end")
    elif selection == 4:
        data = int(input("Enter the node value: "))
        sll.search_node(data)
    elif selection == 5:
        ref_node_data = int(input("Enter the value of ref node: "))
        data = int(input("Enter the new node value: "))
        sll.insert_before_node(ref_node_data, data)
    elif selection == 6:
        ref_node_data = int(input("Enter the value of ref node: "))
        data = int(input("Enter the new node value: "))
        sll.insert_after_node(ref_node_data, data)
    elif selection == 7:
        pass
    elif selection == 8:
        position = int(input("Enter the position: "))
        data = int(input("Enter the new node value: "))
        sll.insert_node_position(position, data)
    elif selection == 9:
        sll.delete_first_node()
    elif selection == 10:
        sll.delete_only_node()
    elif selection == 11:
        ref_node_data = int(input("Enter the node value that needs to be deleted: "))
        sll.delete_between_node(ref_node_data)
    elif selection == 12:
        sll.delete_last_node()

