# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    path = []
    searchNode(tree.left, node, path)


def searchNode(tree, node, path):
    if tree.left is not None:
        searchNode(tree.left, node, path)
        path.append(tree.value)
    