def maxSumIncreasingSubsequence(array):
    answer = [float("-inf")]
    for idx in range(len(array)):
        temp = compare_with_lower(array[:idx+1])
        if temp[0] > answer[0]:
            answer = temp
    return answer

def compare_with_lower(array):
    reverse_arr = array[::-1]
    current_lowerst = float("inf")
    total = float('-inf')
    lst = []
    for num in reverse_arr:
        if num < current_lowerst:
            temp = total
            temp += num
            if temp >= total:
                lst.append(num)
                if total == float("-inf"):
                    total = num
                    current_lowerst = num
                else:
                    total += num
                    current_lowerst = num
    return [total, lst[::-1]]




# dict1 = {0:10, 1:70, 2:20, 3:30, 4:50, 5:11, 6:30}
# array = [10,70,20,30,50,11,30]
# array = [-5, -4, -3, -2, -1]
# array = [-1, 1]
array = [8, 12, 2, 3, 15, 5, 7]
# array = [10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]

# print(compare_with_lower(dict1, 2))

print(maxSumIncreasingSubsequence(array))
#answer [110, [10,20,30,50]]

