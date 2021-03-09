'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file_name = 'integers.txt'




with open(file_name, "r") as file:
    try:
        file1 = file.read()
        file2 = file1.split("\n")
        for num in file2:
            num = num *2
            print(num)
    except Exception as e:
        print(f"{e}")



    # print(file2)
