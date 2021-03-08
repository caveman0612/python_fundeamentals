connections = [(1,6), (6,7), (7,2), (7,8), (8,3), (3,4), (4,5), (5,10), (10,15), (9,14), (13,14), (12,13), (11,12)]

def find(start, end, connections):
    connect = union(connections)
    if connect[start] == connect[end]:
        return True
    return False


def union(connections, high=15):
    dict_connections = {}
    for val in range(1, high + 1):
        dict_connections[val] = val
    # print(connections)
    beenFlipped = []
    for item in connections:
        if dict_connections[item[0]] == dict_connections[item[1]]:
            continue
        else:
            if dict_connections[item[1]] in beenFlipped:
                dict_connections[item[0]] = dict_connections[item[1]]
            else:
                dict_connections[item[1]] = dict_connections[item[0]]
                beenFlipped.append(dict_connections[item[1]])
    return dict_connections

print(find(1, 11, connections))