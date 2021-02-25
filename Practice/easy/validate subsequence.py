#should do a counter that skips if and subtracts based off the sequence and the array
#use while len(sequence) < counter or something like that

def isValidSubsequence(array, sequence):
    counter_s = 0
    counter_a = 0
    list = []
    while counter_s <= len(sequence):
        if counter_s == len(sequence):
            new_array = array[:len(sequence)]
            if sequence == new_array:
                return True
            else:
                return False
        if sequence[counter_s] == array[counter_a]:
            counter_s += 1
            counter_a += 1
        else:
            array.pop(counter_a)

# array = [5,1,22,25,6,-1,8,10]
# sequence = [1, 6, -1, 10]
array = [1,1,1,1,1]
sequence = [1,1,1]
print(isValidSubsequence(array, sequence))