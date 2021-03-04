def nonConstructibleChange(coins):
    coins.sort()

    currentChangeCreated = 0
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        currentChangeCreated += coin
    return currentChangeCreated + 1

coins = [5, 7, 1, 1, 2, 3, 22]
print(nonConstructibleChange(coins))


# def list_function(list):
#     new_list = []
#     for i in range(len(list)):
#         new_list.append(list.copy())
#     for index, value in enumerate(new_list):
#         value.pop(index)
#     return new_list

# def nonConstructibleChange(coins):
#     go = True
#     coins.sort()
#     #initial list seperate
#     main_list = list_function(coins)
#     new_list1 = []
#     new_list2 = []
#     big_list = []
#     switch = True
#     switch1 = True
#     for l3 in main_list:
#         num3 = sum(l3)
#         if num3 in big_list:
#             continue
#         big_list.append(num3)
#     while go:
#         if switch:
#             for value in main_list:
#                 lists = list_function(value)
#                 for l in lists:
#                     num = sum(l)
#                     if num in big_list:
#                         continue
#                     big_list.append(num)
#                 new_list1.extend(lists)
#             main_list.extend(new_list1)
#             switch = False
#         else:
#             if switch1:
#                 new_list2 = []
#                 for value1 in new_list1:
#                     lists1 = list_function(value1)
#                     for l1 in lists1:
#                         num1 = sum(l1)
#                         if num1 in big_list:
#                             continue
#                         big_list.append(num1)
#                     new_list2.extend(lists1)
#                     if len(value1) == 1:
#                         go = False
#
#                 main_list.extend(new_list2)
#                 switch1 = False
#             else:
#                 new_list1 = []
#                 for value2 in new_list2:
#                     lists2 = list_function(value2)
#                     for l2 in lists2:
#                         num2 = sum(l2)
#                         if num2 in big_list:
#                             continue
#                         big_list.append(num2)
#                     new_list1.extend(lists2)
#                     if len(value2) == 1:
#                         go = False
#                 main_list.extend(new_list1)
#                 switch1 = True
#     for i in range(1, sum(coins)):
#         if i not in big_list:
#             # print(i)
#             return i


