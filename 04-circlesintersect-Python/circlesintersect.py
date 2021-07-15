# Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) 
# that takes 6 numbers (ints) -- x1, y1, r1, x2, y2, r2 -- 
# that describe the circle centered at (x1,y1) with radius r1, 
# and the circle centered at (x2,y2) with radius r2, and returns True 
# if the two circles intersect and False otherwise.

import math
def distance(x1,y1,x2,y2):
	return (math.sqrt((x2-x1)**2 + (y2-y1)**2))

def fun_circlesintersect(x1, y1, r1, x2, y2, r2):
	d = distance(x1,y1,x2,y2)
	if r1<0 or r2<0:
		return False
	if d <= r1+r2:
		return True
	else:
		return False
