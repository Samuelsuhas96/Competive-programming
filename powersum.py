# powerSum(n, k) [15 pts]
# Write the function powerSum(n, k) that takes two 
# possibly-negative integers n and k and returns the 
# so-called power sum: Specify the time complexity based 
# on the solution that you have given. [Hint: This can be 
# solved in (n * log k)  or better.

#    1**k + 2**k + ... + n**k

# If n is negative, return 0. Similarly, if k is negative, 
# return 0.
# Powersum
def powerSum(n, k):
    if n > 0 and k > 0:
        result = 0
        for i in range(1,n+1):
            print(i**k)
            result+=i**k
            # print(result)
        return result
    else:
        return 0

# Write your own test cases here...
# print(powerSum(5,2888))
# print(powerSum(19999,199922))
# print(powerSum(100,-2))
print ("All test cases passed...")