#/usr/bin/python3

'''
Problem 1 
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 

The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''
# define 

def mult_sum(number):
    # create a list with numbers multiples of 3 and 5
    num_to_sum = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            # print(i)
            num_to_sum.append(i)
    # sum numbers in list
    return sum(num_to_sum)

print(mult_sum(1000))