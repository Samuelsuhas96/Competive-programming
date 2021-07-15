# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.

import math
def dist(x1,y1,x2,y2):
	result = math.sqrt((x2-x1)**2 + (y2-y1)**2)
	return result

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	# a = dist(x1,y1,x2,y2)
	# b = dist(x1,y1,x3,y3)
	# c = dist(x2,y2,x3,y3)
	# s = (a+b+c)/2

	# return (math.sqrt(s*(s-a)*(s-b)*(s-c)))
	return ((x1*((y2-y3))+x2*((y3-y1))+x3*((y1-y2)))/2)