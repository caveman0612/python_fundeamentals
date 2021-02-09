'''
Write a script that creates a list of all unique values in a list. For example:


unique_list = [55, 'hi', 4, 13]


'''
old_list = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

new_list = []
doubles = []

#finding extras
for item in old_list:
    if item in new_list:
        if item in doubles:
            continue
        else:
            doubles.append(item)
    else:
        new_list.append(item)

#removing extras from main list
for items in doubles:
    new_list.remove(items)

print(new_list)