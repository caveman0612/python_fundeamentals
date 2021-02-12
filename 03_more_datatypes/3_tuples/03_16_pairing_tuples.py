'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
new_list = []
list_numbers = [1, 3, 5, 6, 7, 8, 3, 5]

list_numbers.sort()


if len(list_numbers) % 2 != 0:
    list_numbers.append(0)

for index, num in enumerate(list_numbers):
    if index % 2 != 0:
        continue
    else:
        new_tuple =(num, list_numbers[index + 1])
        new_list.append(new_tuple)

print(new_list)