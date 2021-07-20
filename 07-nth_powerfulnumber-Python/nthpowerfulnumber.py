# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

import math

def prime_check(number):
	count = 2
	if(number == 2 ):
		return True
	elif number == 1 or (number %2 == 0):
		return False
	else:
		for i in range(2,number):
			if number%i == 0:
				count += 1
		if count == 2:
			return True
		return False


def Powerfulnumber(number):
	l =   []
	count = 0
	for i in range(1,number+1):
		if number%i == 0:
			# print(i)
			if prime_check(i):
				# print(i)
				l.append(i)
				if number%(i**2) == 0:
					# print(i)
					count+=1
	# print(l)
	if (len(l)!= 0 and count!=0) and len(l) == count:
		return True
	else:
		return False


def nthpowerfulnumber(n):
	i = 0
	count = 0
	if n == 0:
		return 1
	else:
		while(count<=n-1):
			i = i+1
			if Powerfulnumber(i):
				print(i,Powerfulnumber(i))
				count+=1
		print(count)	
		return i

# print(prime_check(2))
# print(Powerfulnumber(20))
print(nthpowerfulnumber(53))
