# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!


def digit(n):
	result = []
	while(n>=1):
		a = n%10
		result.insert(0,a)
		n = n//10
	return result


def prime(n):
    count = 2
    if n == 2:
        return True
    elif n == 1 or n%2 == 0:
        return False
    else:
        for i in range(3,n,2):
            if n%i == 0:
                count+=1
                if count > 2:
                    return False
        if count == 2:
            return True

def ishappynumber(n):
	# print(a)
	if n<=0:
		return False
	else:
		while( n != 1):
			l = digit(n)
			# print(l)
			sum = 0
			for i in l:
				sum += i**2
			n = sum
			# print(n)
			if n == 4:
				return False
		return True


def ishappyprimenumber(n):
	if ishappynumber(n):
		if prime(n):
			return True
		else:
			return False
	else:
		return False
    

print(prime(833))
print(ishappynumber(833))
# print(ishappyprimenumber())