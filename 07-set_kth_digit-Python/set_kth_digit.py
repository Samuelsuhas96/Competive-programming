# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
		# print(n,k,d)
		s="" 
		s1=""
		s2 =""
		negative = False
		if n<0:
			s = str(abs(n))
			negative = True
		else:
			s = str(n)
		if len(s) > k:
			s1 = s[::-1]
			# print(s1[k])
			v = s1[k]
			v1 = str(d)
			a = s1.replace(v,v1)
			# print(a)
			s2 = a[::-1]
			# print(s2)
			if negative == True:
				return -(int(s2))
			else:
				return int(s2)
		elif (len(s) <= k):
			s3 = "0"*(k-(len(s)-1)) + s
			# print(s3)
			s1 = s3[::-1]
			# print(s1[k])
			v = s1[k]
			v1 = str(d)
			a = s1.replace(v,v1)
			# print(a)
			s2 = a[::-1]
			# print(s2)
			if negative == True:
				return -(int(s2))
			else:
				return int(s2)

print(fun_set_kth_digit(-168,3,1))

