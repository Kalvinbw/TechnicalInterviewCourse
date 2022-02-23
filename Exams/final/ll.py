# return middle node of single linked list
# if even upper middle if even length
# return value

class Node:
    def __init__(self, data = None, next=None): 
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):  
        self.head = None
  
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode


    def find_mid(self):
        if not self.head:
            return None
        
        len = 0
        curr = self.head
        while curr:
            curr = curr.next
            len += 1
        
        mid = (len // 2) + 1

        curr = self.head
        prev = None
        i = 1
        while i < mid:
            prev = curr
            curr = curr.next
            i += 1

        prev.next = curr.next
        return prev.next.data




LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.insert(6)

print(LL.find_mid())