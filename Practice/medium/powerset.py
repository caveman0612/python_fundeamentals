def powerset(array):
    answer = []
    queue = []
    queue.append(array)
    while len(queue) > 0:
        temp = queue.pop(0)
        if temp not in answer:
            answer.append(temp)
        temp_lists = deleteOne(temp)
        queue.extend(temp_lists)
    return answer

def deleteOne(array):
    return_list = []
    for idx in range(len(array)):
        new_array = array.copy()
        new_array.pop(idx)
        return_list.append(new_array)
    return return_list

array = [1,2,3,4,5]
# answer = deleteOne(array)
answer = powerset(array)

print(answer)

# def powerset(array):
#     answer = [array]
#     list1 = []
#     list2 = []
#     go = True
#     main_switch = True
#     second_switch = True
#     while go:
#         if main_switch:
#             temp = deleteOne(array)
#             list1.extend(temp.copy())
#             answer.extend(list1.copy())
#             main_switch = False
#         else:
#             if second_switch:
#                 for item in list1:
#                     temp2 = deleteOne(item)
#                     if len(item) <= 1:
#                         go = False
#                     else:
#                         for things in temp2:
#                             if things in answer or things in list2:
#                                 continue
#                             else:
#                                 list2.extend(temp2.copy())
#
#                 list1 = []
#                 answer.extend(list2)
#                 second_switch = False
#             else:
#                 for item1 in list2:
#                     temp1 = deleteOne(item1)
#                     if len(item1) <= 1:
#                         go = False
#                     else:
#                         for things1 in temp1:
#                             if things1 in answer or things1 in list1:
#                                 continue
#                             else:
#                                 list1.extend(temp1.copy())
#                 list2 = []
#                 answer.extend(list1)
#                 second_switch = True
#     return answer
#
#


# def powerset(array):
#     all_sets = []
#     all_sets.append(array)
#     switch = True
#     while switch:
#         for item in all_sets:
#             if isinstance(item, list):
#                 new_sets = deleteOne(item)
#                 for idx, item1 in enumerate(new_sets):
#                     if item1 in all_sets:
#                         continue
#                     else:
#                         all_sets.extend(item1)
#             else:
#                 switch = False
#                 if item in all_sets:
#
#                     continue
#                 else:
#                     all_sets.extend(item)
#
#     return all_sets
#

