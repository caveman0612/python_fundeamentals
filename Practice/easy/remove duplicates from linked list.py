# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    # def __str__(self):
    #     return self.value


def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        nextNode = currentNode.next
        while nextNode is not None and nextNode.value == currentNode.value:
            nextNode = nextNode.next
        currentNode.next = nextNode
        currentNode = nextNode
    return linkedList

def printLinkedList(linkedList):
    list1 = []
    currentNode = linkedList
    nextNode = currentNode.next
    while nextNode is not None:
        list1.append(currentNode.value)
        currentNode = nextNode
        nextNode = currentNode.next
        if nextNode is None:
            list1.append(currentNode.value)

    return list1

myList = LinkedList(1)
myList.next = LinkedList(2)
myList.next.next = LinkedList(3)
myList.next.next.next = LinkedList(4)
myList.next.next.next.next = LinkedList(4)
myList.next.next.next.next.next = LinkedList(4)
myList.next.next.next.next.next.next = LinkedList(5)
myList.next.next.next.next.next.next.next = LinkedList(6)
myList.next.next.next.next.next.next.next.next = LinkedList(7)

new_list = removeDuplicatesFromLinkedList(myList)
# print(new_list)

print(printLinkedList(new_list))