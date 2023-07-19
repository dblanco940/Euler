

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99
Find the largest palindrome made from the product of two 3-digit numbers.

Ref:

three digits numbers: 

100 - 999
'''

# start multiplying two 3-digit numbers and evaluate if it's a palindrome. 
# add them to a list and define who is bigger 

three_digit_number = range(100, 999)

palindromes = []

for number1 in three_digit_number:
    # print(number1)
    for number2 in three_digit_number:
        number = str(number1 * number2)
        if number == number[::-1]:
            palindromes.append(int(number))

            highest = max(palindromes)
            
            if int(number) == highest:
                x_number1 = number1
                x_number2 = number2                                        
        
print(f'{x_number1} X {x_number2} = {highest}')


