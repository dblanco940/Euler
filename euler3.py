
'''
Problem 3 

The prime factors of 13195 are 5, 7, 13 and 29
What is the largest prime factor of the number $600851475143?

'''

def find_factors(number):
    factors = (i for i in range(1, number) if number % i == 0)
    return factors 


def is_prime_number(anumber):
    # define whether the number given is prime or not
    for i in range(2, anumber):
        if anumber % i == 0:
            print(i)
            # Number is not prime
            return False             
        else: 
            return True
                            

def get_highest_prime_factor(target_number):
    
    prime_factors = [factor for factor in find_factors(target_number) if is_prime_number(factor)]
    
    return prime_factors
    
    
        
    # print(f'Prime Factors: {prime_factors}')
    # return max(prime_factors)

print(get_highest_prime_factor(600851475143))
# print(get_highest_prime_factor(13195))

    
        
