# Additive primes can be defined as prime numbers where the sum of its digits is a prime number. Write a function isAdditivePrime that takes n as an integer and returns True if n is an Additive Prime and False otherwise.
# Some of the Additive Primes are 2, 3, 5, 7, 11, 23, 29, and etc.
# 29 = 2 + 9 = 11 = 1 + 1 = 2 and 2 is a prime number.

def prime(n):
    count = 2
    if n==1 or n<0 or n%2 == 0:
        return False
    elif n == 2:
        return True
    else:
        for i in range(3,n,2):
            if n%i == 0:
                count+=1
        if count == 2:
            return True
        elif count > 2:
            return False
            
def sum_of_digits(n):
    sum = 0
    while(n>0):
        a = n % 10
        sum += a
        n = n // 10
    return sum

def isAdditivePrime(n):
    while(True):
        if prime(n):
            sum = sum_of_digits(n)
            if prime(sum):
                # print(sum)
                return True
            else:
               return False
        else: 
            return False

# print(prime(4))
# print(sum_of_digits(123))
# print(isAdditivePrime(290))
# assert (isAdditivePrime(2) == True
