# Write code for a node and an insert function to create a binary tree
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

    def insert(self, value):
        if value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
    
    def search(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.left is None:
                return False
            else:
                return self.left.search(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(value)

    def printInOrder(self):
        if self.left is not None:
            self.left.printInOrder()
        print(self.data)
        if self.right is not None:
            self.right.printInOrder()
        


root = Node(10)
root.insert(8)
root.insert(17)
root.insert(5)
root.insert(9)
root.insert(14)
print(root.search(5))
print(root.search(3))

root.printInOrder()