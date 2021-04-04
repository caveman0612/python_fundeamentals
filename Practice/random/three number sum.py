def threeNumberSum(array, targetSum):
    answer = []
    array.sort()
    current = 0
    next = 1
    end = len(array) - 1
    while current < len(array) - 2:
        if next >= end:
            current += 1
            next = current + 1
            end = len(array) -1
        temp = array[current] + array[next] + array[end]
        if temp == targetSum:
            answer.append([array[current], array[next], array[end]])
            next += 1
        elif temp < targetSum:
            next += 1
        elif temp > targetSum:
            end -= 1
    return answer







array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
answer = threeNumberSum(array, targetSum)
print(answer)

