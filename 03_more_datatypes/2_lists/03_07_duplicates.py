'''

Write a script that removes all duplicates from a list.

'''

list_1 = [1, 4, 2, 6, 3, 4, 3, 4, 5]
print(type(list_1))

new_list = set(list_1)
old_list = list(new_list)
old_list.sort()
print(old_list)
