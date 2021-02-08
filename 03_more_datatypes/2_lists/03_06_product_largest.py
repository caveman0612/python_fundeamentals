'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
# list_num_1 = [1,2,3,4,5,6,7,8,9,7]
list_num = []
sum = 0
for i in range(10):
    num = input(f"input {i+1} number")
    list_num.append(num)
    sum += int(num)

list_num.sort()
print(list_num[-1])
print(sum)
