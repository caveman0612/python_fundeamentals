# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None




def branchSums(tree):
    current_sum = 0
    global answer
    answer = []
    search_func(tree, current_sum)
    return answer

def search_func(tree, current_sum):
    if tree.right == None and tree.left == None:
        answer.append(current_sum + tree.value)
    if tree.right != None and tree.left != None:
        current_sum1 = tree.value + current_sum
        search_func(tree.left, current_sum1)
        search_func(tree.right, current_sum1)
    if tree.left != None and tree.right == None:
        current_sum1 = tree.value + current_sum
        search_func(tree.left, current_sum1)
    if tree.right != None and tree.left == None:
        current_sum1 = tree.value + current_sum
        search_func(tree.right, current_sum1)

BT = BinaryTree(1)
BT.left = BinaryTree(2)
BT.right = BinaryTree(3)
BT.left.left = BinaryTree(4)
BT.left.right = BinaryTree(5)
BT.right.left = BinaryTree(6)
BT.right.right = BinaryTree(7)
BT.left.left.left = BinaryTree(8)
BT.left.left.right = BinaryTree(9)
BT.left.right.left = BinaryTree(10)

print(branchSums(BT))

