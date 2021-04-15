def maxSumIncreasingSubsequence(array):
    high_idx = 0
    sums = [num for num in array]
    prev_lists = [None for num in array]
    for i in range(len(array)):
        current_num = array[i]
        for j in range(0, i):
            prev_num = array[j]
            if prev_num < current_num and current_num + sums[j] >= sums[i]:
                sums[i] = current_num + sums[j]
                prev_lists[i] = j
        if sums[i] >= sums[high_idx]:
            high_idx = i
    return [sums[high_idx], build_list(array, prev_lists, high_idx)]

def build_list(array, prev_list, high_idx):
    answer = []
    while high_idx is not None:
        answer.append(array[high_idx])
        high_idx = prev_list[high_idx]
    answer = answer[::-1]
    return answer






# array = [10,70,20,30,50,11,30]
array = [-5, -4, -3, -2, -1]
# array = [1]
# array = [8, 12, 2, 3, 15, 5, 7]
# array = [10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]

# print(compare_with_lower(dict1, 2))

print(maxSumIncreasingSubsequence(array))

