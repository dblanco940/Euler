from itertools import count, islice


'''
https://projecteuler.net/problem=5

answer : 232792560
'''

div_by = list(range(1,21))

# define if a nunber is divisible by all numbers in a given list 
def all_divisible(number):
    if all((number % i == 0) for i in div_by):
        return True
    else:
        return False
# using count() to iterate over an infinite list of numbers and islice to 
# get the first positive number in the generated list (bypassing cero which is fist in the list)
smallest_divisible = islice((i for i in count() if all_divisible(i)), 1, 2)

print(list(smallest_divisible))
