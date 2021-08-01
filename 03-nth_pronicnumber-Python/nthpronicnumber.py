# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def nthpronicnumber(n):
	count = 0 
	i = 1
	if n == 0:
		return 0
	else:
		while(True):
			j = i + 1
			result = i*j
			count += 1
			if count == n:
				return result
			i += 1
			
