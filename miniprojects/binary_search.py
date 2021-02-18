sorted_list = [1, 3, 3, 4, 7, 7, 7, 9, 10, 10, 10, 10, 10, 11, 11, 12, 13, 15, 15, 16, 16, 17, 17, 18, 19, 21, 21, 21, 21, 21, 22, 25, 27, 28, 28, 29, 31, 33, 34, 35, 37, 39, 40, 41, 42, 43, 44, 45, 46, 48, 48, 48, 49, 49, 50, 51, 51, 51, 52, 52, 52, 53, 53, 53, 53, 54, 54, 57, 58, 59, 61, 62, 62, 62, 64, 66, 69, 71, 73, 74, 76, 81, 83, 85, 85, 87, 88, 88, 89, 90, 90, 92, 95, 95, 95, 96, 97, 99, 99, 99]


def binary_Search(target, list):
    length = len(list)
    half = int(length/2)
    pivot = list[half]

    if length == 1 and pivot != target:
        return False
    if pivot == target:
        return True
    elif pivot < target:
        search = binary_Search(target, list[half:])
        return search
    elif pivot > target:
        search = binary_Search(target, list[:half])
        return search


search = binary_Search(2, sorted_list)
print(search)
