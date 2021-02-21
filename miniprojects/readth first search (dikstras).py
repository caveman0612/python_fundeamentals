path_map = {"a": {"b": 4, "c": 2},
            "b": {"a": 4, "c": 1, "d": 5},
            "c": {"a": 2, "b": 1, "d": 8, "e": 10},
            "d": {"b": 5, "c": 8, "e": 2, "z": 6},
            "e": {"c": 10, "d": 2, "z": 5},
            "z": {"e": 5, "d": 6},
            }

# path_map = {"a": {"b": 4, "c": 2},
#             "b": {"a": 4, "d": 5},
#             "c": {"a": 2, "e": 10},
#             "d": {"b": 5, "z": 6},
#             "e": {"c": 10, "z": 5},
#             "z": {"e": 5, "d": 6},
#             }




def dijkstra_algo(start, end):
    cur_node = start
    next_node = ""
    path_dict = {}
    current_path = 0
    while cur_node != end:
        if len(path_dict) == 0:
            options = path_map[cur_node]
            options = dict(sorted(options.items(), key=lambda items: items[1]))
            for key, value in options.items():
                path_dict[cur_node + key] = value
            string1 = list(options.keys())[0]
            current_path = list(path_dict.keys())[0]
            cur_node = string1[-1]


        elif len(path_dict) > 0:
            options1 = path_map[cur_node]
            options1 = dict(sorted(options1.items(), key=lambda items: items[1]))
            first_index = list(path_dict.keys())[0]
            old_distance = path_dict[first_index]
            for key, value in options1.items():
                if key == start:
                    continue
                elif key not in path_dict:
                    path_dict[current_path + key] = value + old_distance
                else:
                    path_dict[current_path + key] += value + old_distance
            path_dict = dict(sorted(path_dict.items(), key=lambda items: items[1]))
            path_dict.pop(current_path)
            string2 = list(path_dict.keys())[0]
            cur_node = string2[-1]
            current_path = list(path_dict.keys())[0]

    # print(current_path)
    # print(cur_node)
    print(path_dict)

    answer = list(path_dict.items())[0]
    return answer


answer = dijkstra_algo("a", "z")
print(answer)

# def dijkstra_algo(start, end):
#     node = start
#     next_node
#     path_dict = {}
#     counter = 0
#     while node != end:
#         prospects = path_map[node]
#         temp_node = ""
#         weight = 0
#         for key, values in prospects.items():
#             if key in path_dict:
#                 new_key =
#             if weight == 0:
#                 weight = values
#                 temp_node = key
#             elif values < weight:
#                 weight = values
#                 temp_node = key
#             path_dict[key] = values
#             path_dict = dict(sorted(path_dict.items() , key=lambda items: items[1]))
#         node = temp_node
#
#         # counter += 1
#         # if counter == 5:
#         #     node = end
#     print(path_dict)




# def dijkstra_algo (start, end):
#     path = [start,]
#     temp_dict = {}
#     already_traveled = [start,]
#     for key, value in path_map.items():
#         if key == start:
#             for key1, value1 in value.items():
#                 temp_dict[key1] = value1
#                 temp_dict = dict(sorted(temp_dict.items(), key=lambda items: items[1]))
#
#     for i in range(4):
#         keys = list(temp_dict.keys()) # c
#         list_values = list(temp_dict.values()) # 2
#         new_location = path_map.get(keys[0])
#
#
#         for key2, value in new_location.items():
#             if key2 in already_traveled:
#                 continue
#             temp_dict[key2] = value + list_values[0]
#
#         temp_dict.pop(keys[0])
#         already_traveled.append(keys[0])
#         temp_dict = dict(sorted(temp_dict.items(), key=lambda items: items[1]))
#
#
#     print(temp_dict, already_traveled)



