# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	d = {}
	for i in s:
		if s.count(i) in d:
			# d[s.count(i)].append(i)
			if i in d[s.count(i)]:
				continue
			else:
				d[s.count(i)].append(i)
		else:
			d[s.count(i)] = [i]
	print(d)
	print(sorted(d,reverse= True))
	a = sorted(d,reverse= True)
	print(a)
	count = 1
	if n > max(a):
		return d[min(a)][0]
	else:
		for j in a:
			if n == count:
				return (d[j][0])
			else:
				count += 1



print(fun_kth_occurrences("asuszenphonemaxm1 aemnsh", 6))



