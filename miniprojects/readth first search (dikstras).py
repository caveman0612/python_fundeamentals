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

# should look into: if the path wants to go somewhere its already gone before that should be skipped or canceled


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




