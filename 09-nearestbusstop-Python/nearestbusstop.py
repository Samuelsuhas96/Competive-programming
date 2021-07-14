# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def look(street,v):
	first = street - v
	second = v+8 - street
	if first <= second:
		return v
	else:
		return v+8

	# for i in l:
	# 	if street < i:
	# 		a = street - i
	# 		b = (i+8) - street
	# 		if a>b:
	# 			return b
	# 		else:
	# 			return a
	# 	else:



def fun_nearestbusstop(street):
	if street == 0:
		return 0
	l = []
	for i in range(0,street,8):
		l.append(i)
	# print(l)
	# print(look(street,l))
	return look(street,l[-1])


# print(fun_nearestbusstop(13))