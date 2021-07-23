# Write a function isPalindromicPrime that takes a value n as a parameter and returns True if the given n is a palindrome and prime and False otherwise.

def prime_check(n):
    count = 2
    if n == 2:
        return True
    elif n == 1 or n%2 == 0:
        return False
    for i in range(3,n):
        if n%i == 0:
            count += 1
    if count > 2:
        return False
    else:
        return True

def pallindrome_check(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False

def ispallindromicprime(n):
    if pallindrome_check(n):
        if prime_check(n):
            return True
        else:
            return False
    else:
        return False
    

print(prime_check(-1))
# print(pallindrome_check(121))
# print(ispallindromicprime(373))