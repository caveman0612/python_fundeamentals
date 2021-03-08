def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):
    # check current value
    if tree is None:
        print(type(tree))
        return closest
    # check the difference between target and current value compared to closest value
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    # if target is smaller search left side of tree with helper
    if target < tree.value:
        print(type(tree))
        return findClosestValueInBstHelper(tree.left, target, closest)
    # elif target is larger search right side
    elif target > tree.value:
        print(type(tree))
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        print(type(tree))
        return closest



# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data):
        pass

tree = BST(10)
tree.right = BST(15)
tree.right.left = BST(13)
tree.right.left.right = BST(14)
tree.right.right = BST(22)
tree.left = BST(5)
tree.left.left = BST(2)
tree.left.right = BST(5)
tree.left.left.left = BST(1)


target = 4
print(findClosestValueInBst(tree, target))