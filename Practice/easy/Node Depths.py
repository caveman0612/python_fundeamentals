def nodeDepths(root):
    global total
    total = 0
    nodeDepthHelper(root)
    print(total)
    return total

def nodeDepthHelper(root, d=0):
    depth = d + 1
    if root.left == None and root.right == None:
        global total
        total += depth
    if root.left == None and root.right != None:
        nodeDepthHelper(root.left, depth)
    if root.left != None and root.right == None:
        nodeDepthHelper(root.right, depth)
    if root.left != None and root.right != None:
        nodeDepthHelper(root.left, depth)
        nodeDepthHelper(root.right, depth)



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


