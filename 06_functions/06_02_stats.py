'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(list):
  sum = 0
  maxi = max(list)
  mini = min(list)
  length = len(list)
  for num in list:
    sum += num
  print(maxi, mini, sum/length, sum)

# call the function below here
stats(example_list)