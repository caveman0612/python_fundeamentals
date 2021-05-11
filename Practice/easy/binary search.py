def binarySearch(array, target, idx=0):
    length = len(array)
    half = int(length / 2)
    value = array[half]
    if value > target:
        #take idx and subtract from len(array) to get difference
        num1 = ((length - half) + idx)
        return binarySearch(array[:half], target, )
    elif value < target:
        #add idx to half
        num2 = half + idx
        return binarySearch(array[half:], target, num2)
    elif value == target:
        return target, idx

    return -1



#     switch = True
#     while len(array)>1:
#         half = int(len(array)/2)
#         temp = array[half]
#         if array[half] == target:
#             return half
#         elif array[half] < target:
#             array = array[half:]
#         elif array[half] > target:
#             array = array[:half]
#     return -1

array = [1,5,7,9,11,15,16,22,35]
target = 7
print(binarySearch(array, target))
