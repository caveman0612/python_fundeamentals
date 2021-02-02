'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

def miles_to_kilometers(miles):
    return miles * 1.6

answer = miles_to_kilometers(10)/30.5
print(answer)

print(f"He was running {answer} kilometers per hour")