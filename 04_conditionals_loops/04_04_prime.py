'''
Print out every prime number between 1 and 100.

'''
dict_primes = {}

for i in range(1, 101):
    for x in range(1, i):
        if i % x == 0:
            if i not in dict_primes:
                dict_primes[i] = 1
            else:
                dict_primes[i] += 1
for key, values in dict_primes.items():
    if values == 1:
        print(key)