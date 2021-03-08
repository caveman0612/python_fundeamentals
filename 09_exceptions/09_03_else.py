'''
Write a script that demonstrates a try/except/else.

'''
try:
    num = open("integers.txt", "r")
    num1 = num.read()
except:
    print("failed")
else:
    print(num1)
finally:
    num.close()