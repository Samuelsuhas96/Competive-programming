# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

def handtodice(hand):
	# a = hand%10 # for the last digit/dice
	# r = hand//10
	# b = r%10 # for the second digit/dice
	# c = r//10 # for the first digit/dice
	r = []
	# c = len(str(hand))
	# hand = str(hand)
	# while(len(hand) >=0):
	# 	hand = int(hand)
	# 	# print(hand)
	# 	# to retrieve the digits as they are.
	# 	t = hand // 10**(c-1)
	# 	# print(t)
	# 	r.append(t)
	# 	if(hand == 0):
	# 		break
	# 	hand = hand % 10**(c-1)
	# 	hand = str(hand)
	# 	# print(hand)
	# r.append(0)
	# return tuple(r)
	while(hand != 0):
		a = hand % 10
		r.append(a)
		hand = hand // 10
	return tuple(r[::-1])

print(handtodice(422))
		



	

