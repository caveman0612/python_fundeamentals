def productSum(array, depth=0):
    total_sum = 0
    depth += 1
    for item in array:
        if isinstance(item, int):
            total_sum += item
        if isinstance(item, list):
            temp = productSum(item, depth) * (depth + 1)
            total_sum += temp
    return total_sum

# def productSumHelper(array, depth):
#     total_sum = 0
#     depth += 1
#     for item in array:
#         if isinstance(item, int):
#             total_sum += item
#         if isinstance(item, list):
#             temp = productSumHelper(item, depth) * (depth + 1)
#             total_sum += temp
#     return total_sum

array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
answer = productSum(array)
print(answer)