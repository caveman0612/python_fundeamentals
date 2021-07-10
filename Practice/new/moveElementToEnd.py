def moveElementToEnd(array, toMove):
    if len(array) == 0:
        return array
    i = 0
    j = len(array) - 1
    while i != j:
        if array[i] == toMove:
            array.append(array.pop(i))
            j -= 1
        else:
            i += 1
    return array





array = [2, 1, 2, 2, 2, 3, 4, 2]
value = 2
print(moveElementToEnd(array, value))