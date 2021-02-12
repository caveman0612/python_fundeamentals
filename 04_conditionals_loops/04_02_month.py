'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
list = ["January", "February", "March", "April", "May", "June", "July", "Auguest", "September", "October", "November", "December"]

month = input("input number for month")

month = int(month) - 1

if month > -1 and month < 12:
    print(list[month])
else:
    print("outside of range")



