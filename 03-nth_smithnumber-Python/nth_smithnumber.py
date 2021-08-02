# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def sum_of_digits(n):
    sum = 0
    while(n>0):
        a = n%10
        sum = sum + a
        n = n//10
    return sum

def composite_check(n):
    count = 2
    if n == 2:
        return False
    elif n == 1 or n % 2 == 0:
        return True
    else:
        for i in range(3,n,2):
            if n%i == 0:
                count += 1
        if count > 2:
            return True
        else:
            return False

def prime_check(n):
    count = 2
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    else:
        for i in range(3,n,2):
            if n%i == 0:
                count += 1
        if count > 2:
            return False
        else:
            return True

def fun_nth_smithnumber(n):
    count = 0
    i = 2
    prime_factor_sum = 0
    while(True):
        # print(i)
        if composite_check(i):
            print(i)
            for j in range(2,i):
                if i%j == 0:
                    if prime_check(j):
                        print("primefactor: ",j)
                        prime_factor_sum+=sum_of_digits(j)
                        # print(prime_factor_sum)
            print(i,prime_factor_sum,sum_of_digits(i))
            if sum_of_digits(i) == prime_factor_sum:
                count += 1
                if count == n:
                    return i
            # print("yes")
        prime_factor_sum = 0
        i = i + 1

# print(sum_of_digits(123))
# print(composite_check(12))
# print(prime_check(12))
print(fun_nth_smithnumber(2))