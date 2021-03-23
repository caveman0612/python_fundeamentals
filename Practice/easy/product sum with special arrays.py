def productSum(array, depth=1, total_sum = 0):
    for item in array:
        # print(type(item))
        if isinstance(item, int):
            # print("yes")
            total_sum += item
        if isinstance(item, list):
            answer = productSum(item, depth + 1, total_sum)
            return answer * depth
    return total_sum


array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
answer = productSum(array)
print(answer)