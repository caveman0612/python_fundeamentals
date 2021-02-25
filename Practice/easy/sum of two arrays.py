def isValidSubsequence(array, sequence):
    counter = 0
    list = []
    for i, num in enumerate(array):
        if num in sequence:
            list.append(num)
            counter += 1
            if counter == len(sequence) and list == sequence:
                return True
        else:
            continue
    if list == sequence:
        return True
    else:
        return False


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(isValidSubsequence(array, sequence))
# array1 = [1, 1, 1, 1, 1]
# sequence = [1, 1, 1]
# print(isValidSubsequence(array1, sequence))

# def twoNumberSum(array, targetSum):
#     if len(array) < 2:
#         return
#     for i, num in enumerate(array):
#         for i1, num1 in enumerate(array):
#             sum = num + num1
#             if i == i1:
#                 continue
#             elif sum == targetSum:
#                 return [num, num1]
#
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# print(twoNumberSum(array, 10))
