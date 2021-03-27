def smallestDifference(arrayOne, arrayTwo):
    values = []
    differance = None
    for num in arrayOne:
        for num1 in arrayTwo:
            if differance == None:
                differance = abs(num - num1)
                values = [num, num1]
            if abs(num - num1) < differance:
                differance = abs(num - num1)
                values = [num, num1]
    return values



arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
answer = smallestDifference(arrayOne, arrayTwo)
print(answer)