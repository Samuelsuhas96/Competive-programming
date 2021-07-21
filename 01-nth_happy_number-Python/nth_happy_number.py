# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)

def digit(n):
	result = []
	while(n>=1):
		a = n%10
		result.insert(0,a)
		n = n//10
	return result

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

def nth_happy_number(n):
	count = 0
	i = 0
	while(count <= n-1):
		i += 1
		if ishappynumber(i):
			count += 1
	return i

print(nth_happy_number(2))
