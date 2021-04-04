def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    value_1 = 0
    value_2 = 0
    difference = float("inf")
    idx1 = 0
    idx2 = 0
    while idx1 < len(arrayOne) and idx2 < len(arrayTwo):
        if arrayOne[idx1] == arrayTwo[idx2]:
            return [arrayOne[idx1], arrayTwo[idx2]]
        elif arrayOne[idx1] < arrayTwo[idx2]:
            if arrayTwo[idx2] - arrayOne[idx1] < difference:
                value_1 = arrayOne[idx1]
                value_2 = arrayTwo[idx2]
                difference = arrayTwo[idx2] - arrayOne[idx1]
            idx1 += 1
        elif arrayOne[idx1] > arrayTwo[idx2]:
            if arrayOne[idx1] - arrayTwo[idx2] < difference:
                value_1 = arrayOne[idx1]
                value_2 = arrayTwo[idx2]
                difference = arrayOne[idx1] - arrayTwo[idx2]
            idx2 += 1
    return [value_1, value_2]




arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
# arrayOne.sort()
# arrayTwo.sort()
# print(arrayOne, arrayTwo)
answer = smallestDifference(arrayOne, arrayTwo)
print(answer)


#
# def smallestDifference(arrayOne, arrayTwo):
#     values = []
#     differance = None
#     for num in arrayOne:
#         for num1 in arrayTwo:
#             if differance == None:
#                 differance = abs(num - num1)
#                 values = [num, num1]
#             if abs(num - num1) < differance:
#                 differance = abs(num - num1)
#                 values = [num, num1]
#     return values



