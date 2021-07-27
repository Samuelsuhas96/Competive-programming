# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	if n > 0:
		for i in range(n):
			a = s[0]
			b = s[1:]
			s = b + a
		return s
	else:
		n = abs(n)
		for i in range(n):
			a = s[-1]
			b = s[0:-1]
			s = a + b
		return s

# print(fun_rotatestrings("abcd",1))
# print(fun_rotatestrings("abcd",1))
# print(fun_rotatestrings("abcd",1))
# print(fun_rotatestrings("abcd",1))