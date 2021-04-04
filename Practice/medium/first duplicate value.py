def firstDuplicateValue(array):
    pos2 = float("inf")
    for idx, num in enumerate(array):
        for idx1, num1 in enumerate(array[idx+1:]):
            if num == num1:
                pos_1 = idx
                pos_2 = idx + idx1 + 1
                if pos_2 < pos2:
                    pos2 = pos_2
    if isinstance(pos2, float):
        return -1
    return array[pos2]

array1 = [2,1,5,2,3,3,4]
array2 = [2,1,5,3,3,2,4]
array3 = [2,1,5,3,4]
print(firstDuplicateValue(array2))