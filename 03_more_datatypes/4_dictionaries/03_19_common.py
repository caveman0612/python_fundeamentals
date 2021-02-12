'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:



result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}


new_dictionary = {}

for key, value in dict_1.items():
    if key not in new_dictionary:
        new_dictionary[key] = value
    else:
        new_dictionary[key] += value

for key, value in dict_2.items():
    if key not in new_dictionary:
        new_dictionary[key] = value
    else:
        new_dictionary[key] += value

print(new_dictionary)