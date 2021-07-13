# This is the most complicated part. Write the function playstep2(hand, dice) that plays step 2 as
# explained above. This function takes a hand, which is a 3-digit integer, and it also takes dice,
# which is an integer containing all the future rolls of the dice. For example, if dice is 5341,
# then the next roll will be a 1, then the roll after that will be a 4, then a 3, and finally a 5.
# Note that in a more realistic version of this game, instead of hard-coding the dice in this way,
# we'd probably use a random-number generator.

# With that, the function plays step2 of the given hand, using the given dice to get the next rolls
# as needed. At the end, the function returns the new hand, but it has to be ordered, and the
# function also returns the resulting dice (which no longer contain the rolls that were just used).

# For example:
# assert(playstep2(413, 2312) == (421, 23))
# Here, the hand is 413, and the future dice rolls are 2312. What happens? Well, there are no
# matching dice (pair) in 413, so we keep the highest die, which is a 4, and we replace the 1 and the 3
# with new rolls. Since new rolls come from the right (the one's digit), those are 2 and 1. So the
# new hand is 421. It has to be sorted, but it already is. Finally, the dice was 2312, but we used 2
# digits, so now it's just 23. We return the hand and the dice, so we return (421, 23).

# For Example:
# assert(playstep2(544, 456) == (644, 45))
# If you have 2 matching dice (a pair), keep the pair and roll one die to replace the third die.
# So the output is (644, 45)

# Here are some more examples. Be sure you carefully understand them:
# assert(playstep2(413, 2312) == (421, 23))
# assert(playstep2(413, 2345) == (544, 23))
# assert(playstep2(544, 23) == (443, 2))
# assert(playstep2(544, 456) == (644, 45))
# Hint: You may wish to use handToDice(hand) at the start to convert the hand into the 3 individual
# dice.
# Hint: Then, you may wish to use diceToOrderedHand(a, b, c) at the end to convert the 3 dice back
# into a sorted hand.
# Hint: Also, remember to use % to get the one's digit, and use //= to get rid of the one's digit.

def playstep2(hand, dice):
	forhand=str(hand)
	fordice=str(dice)
	final=[]
	final1=[]
	han=list(map(str,forhand))
	dic=list(map(str,fordice))
	result1=[]
	result2=tuple()
	s=""
	s1=""
	s2=""
	s11=""

	duplicate=set(han)
	if(len(duplicate)==len(han)):
		han.sort()
		larger=han[-1]
		final.append(larger)
		add_dic1=dic[-1]
		final.append(add_dic1)
		add_dic2=dic[-2]
		final.append(add_dic2)
		for j in final:
			s+=j
		for k in sorted(s):
			s1+=k
		s1=s1[::-1]	
		o1="".join(final)
		final=[]
		rest_dic=dic[0:-2]
		rest_dic="".join(rest_dic)
		final.append(s1+','+rest_dic)
		final=("".join(final))
		final=final.split(",")
		res=tuple(list(map(int,final)))
		return res
	else:
		han.sort()
		smaller=han[-2]
		final1.append(smaller*2)
		add_dic1=dic[-1]
		final1.append(add_dic1)
		for j in final1:
			s11+=j
		for k in sorted(s11):
			s2+=k
		s2=s2[::-1]	
		o2="".join(final1)
		final1=[]
		rest_dic=dic[0:-1]
		rest_dic="".join(rest_dic)
		final1.append(s2+','+rest_dic)
		final1=("".join(final1))
		final1=final1.split(",")
		res=tuple(list(map(int,final1)))
		return res

print(playstep2(413,2313))