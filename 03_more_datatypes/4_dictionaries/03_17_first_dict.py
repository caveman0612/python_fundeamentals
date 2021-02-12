'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''
dict = {}
for i in range(1, 11):
    value = input(f"input value for {i} key")
    dict[i] = value

print(dict)