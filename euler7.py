from itertools import count, islice

'''
https://projecteuler.net/problem=7
what is 10001 prime number
'''

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

# print(is_prime(7))
# print(is_prime(10))
# print(is_prime(11))
# print(is_prime(16))
# print(is_prime(17))

def count_prime(cardinal):
    prime_count = []

    for i in count(2):
        if is_prime(i):
            prime_count.append(i)
        if len(prime_count) < cardinal:
            continue
        else:
            break
    return prime_count[-1]


print(count_prime(10001))
        
