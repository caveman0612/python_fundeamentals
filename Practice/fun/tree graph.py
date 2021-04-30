class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert (self, data):
        if self.data:
            print(self.data)

tree = Node(12)
tree.insert(6)