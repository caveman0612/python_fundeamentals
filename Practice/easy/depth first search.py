# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        answer = []
        Node.depthFirstSearch(array.left)

A = Node("A")
B = A.addChild("B")
C = A.addChild("C")
D = A.addChild("D")
E = B.addChild("E")
F = B.addChild("F")
I = F.addChild("I")
J = F.addChild("J")
G = D.addChild("G")
H = D.addChild("H")
K = G.addChild("K")
