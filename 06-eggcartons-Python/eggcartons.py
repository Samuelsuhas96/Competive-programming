# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
	# for the least number of egg cartons
	if eggs == 0:
		return 0
	# for 12 or less number of eggs
	elif eggs <= 12:
		return 1
	# to get cartons for number of eggs that are multiples of 12
	elif (eggs % 12 == 0):
		return eggs // 12 
	# for all the oter cases
	else:
		return (eggs // 12) + 1
