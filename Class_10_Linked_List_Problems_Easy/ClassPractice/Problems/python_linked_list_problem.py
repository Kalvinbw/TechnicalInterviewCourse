# Create a linked list using python
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
        



llist = LinkedList()
llist.append(1)
llist.append(4)
llist.append(5)
llist.append(6)
llist.prepend(-3)
llist.displayList()
print()

llist.reverse()
llist.displayList()
print()

llist.removeNode(6)
llist.removeNode(4)
llist.displayList()
