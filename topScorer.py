# topScorer(data) [10 Points]
# Write the function topScorer(data) that takes a multi-line 
# string encoding scores as csv data for some kind of 
# competition with players receiving scores, so each 
# line has comma-separated values. The first value on 
# each line is the name of the player (which you can 
# assume has no integers in it), and each value after 
# that is an individual score (which you can assume is a 
# non-negative integer). You should add all the scores 
# for that player, and then return the player with the 
# highest total score. If there is a tie, return all the 
# tied players in a comma-separated string with the names 
# in the same order they appeared in the original data. 
# If nobody wins (there is no data), return None (not the 
# string "None"). So, for example:

def topScorer(data):
    d={}
    sum = 0
    print(data)
    a = data.split("\n")
    # print(a)
    if a[0]=="" or a[0] == " ":
        return None
    for i in a:
        if i != '':
            b = i.split(",")
            for j in b[1:]:
                sum += int(j)
            if sum in d:
                d[sum].append(b[0])
            else:
                d[sum] = [b[0]]
            sum = 0
    if max(d):
        if len(d[max(d)]) > 1:
            s = ""
            for k in d[max(d)]:
                s += k+","
            return s[0:-1]
        else:
            return d[max(d)][0]
    print(d)
    return a


data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''

assert(topScorer(data) == 'Fred')

data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
assert(topScorer(data) == 'Wilma')

data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
assert(topScorer(data) == 'Fred,Wilma')

assert(topScorer('') == None)
print("All test cases passed...!")
# Hint: you may want to use both splitlines() and split(',') here!
