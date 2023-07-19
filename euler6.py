from itertools import islice

'''
https://projecteuler.net/problem=6


'''

# The sum of the squares of the first 100 natural numbers:



def sum_of_squares():
    result = 0 
    for i in range(1,101):
        result += i ** 2
    return result

sq_of_sum = sum(list(range(1,101))) ** 2

end_result = sq_of_sum - sum_of_squares() 

# print(sq_of_sum)

print(end_result)

    
