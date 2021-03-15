def nodeDepths(root):
    total = []
    nodeDepthHelper(root, total, 0)
    return sum(total)

def nodeDepthHelper(root, total, depth):
    if root.left == None and root.right == None:
        if depth > 0:
            total.append(depth)
    if root.left == None and root.right != None:
        if depth > 0:
            total.append(depth)
        nodeDepthHelper(root.right, total, (depth+1))
    if root.left != None and root.right == None:
        if depth > 0:
            total.append(depth)
        nodeDepthHelper(root.left, total, (depth+1))
    if root.left != None and root.right != None:
        if depth > 0:
            total.append(depth)
        nodeDepthHelper(root.left, total, (depth+1))
        nodeDepthHelper(root.right, total, (depth+1))

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.right = BinaryTree(3)
tree.left.left = BinaryTree(4)
tree.left.right = BinaryTree(5)
tree.left.left.left = BinaryTree(8)
tree.left.left.right = BinaryTree(9)
tree.right.left = BinaryTree(6)
tree.right.right = BinaryTree(7)

nodeDepths(tree)


