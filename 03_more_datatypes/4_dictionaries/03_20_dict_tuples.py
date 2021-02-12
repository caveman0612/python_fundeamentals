'''
CHALLENGE: Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

NOTE: Check out the Python docs and see whether you can come up with a solution, even if you don't yet
      completely understand _why_ it works the way it does:
      https://docs.python.org/3/howto/sorting.html#key-functions
      Feel free to discuss any questions you have with your mentor and on the forum!

'''

dict = {"item1": 5, "item2": 6, "item3": 1}
list = []

for item in dict.items():
    list.append(item)

#bubble sort
for x in range(len(list) - 1):
    for i in range(len(list) - 1):
        temp = 0
        if list[i][1] > list[i + 1][1]:
            temp = list[i]
            list[i] = list[i + 1]
            list[i + 1] = temp

print(list)
