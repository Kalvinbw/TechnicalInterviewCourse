# Create a linked list using python
from os import curdir


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def remove_dups(self):
        prev = self.head
        current = prev.next

        while current:
            if prev.data == current.data:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
    
    def remove_dups_unsorted(self):
        di = {self.head.data: self.head}

        current = self.head.next
        prev = self.head

        while current:
            if current.data in di:
                prev.next = current.next                
            else:
                di[current.data] = current
                prev = current
            current = current.next

    def remove_skipped_nodes(self, m, n):
        current = self.head
        for _ in range(m-1):
            current = current.next

        
        for _ in range(n):
            current.next = current.next.next


    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        current = self.head

        while current.next != None:
            current = current.next

        newNode = Node(data)
        current.next = newNode
    
    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def removeNode(self, data):
        if self.head == None: return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head

        while current.next != None:
            if current.next.data == data:
                if current.next.next == None:
                    current.next = None
                    return
                else:
                    current.next = current.next.next
                    return
            current = current.next

    def displayList(self):
        current = self.head
        while current.next != None:
            print(current.data)
            current = current.next
        print(current.data)
        

def recursive_reverse(node):
    if node is None:
        return node
    if node.next is None:
        return node
    
    tempnode = recursive_reverse(node.next)
    node.next.next = node
    node.next = None
    return tempnode



llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)
llist.append(7)
llist.append(8)
# llist.prepend(1)
llist.displayList()
print()

# llist.remove_dups_unsorted()
# llist.reverse()

llist.remove_skipped_nodes(2, 1)
llist.displayList()
print()

# llist.removeNode(6)
# llist.removeNode(4)
# llist.displayList()



