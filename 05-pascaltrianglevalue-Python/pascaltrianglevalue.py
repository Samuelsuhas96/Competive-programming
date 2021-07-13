# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 

import math
def value(n,r):
	return(int((math.factorial(n)/(math.factorial(n-r)*(math.factorial(r))))))

def fun_pascaltrianglevalue(row, col):
	# print(value(1,1))
	if(col<=row+1):
		return value(row,col)
	elif(col>row):
		return 0
	else:
		return None

print(fun_pascaltrianglevalue(1,1))