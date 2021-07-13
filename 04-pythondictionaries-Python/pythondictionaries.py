"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""


"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order. Make it function with name as sortUSA(), return list of cities
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this: (Make it function with name as alphaAsia(), return list of cities)
1
American City
American City
2
Asian City - Country
Asian City - Country"""


def sortUSA():
    ''' To just return all the cities in the USA in alphabetical order'''
    if "North America" in locations:
        if 'USA' in locations["North America"]:
            locations['North America']['USA'].sort()
    return locations['North America']['USA']

def alphaAsia():
    result = []
    s = ""
    '''To just return all the cities in Asia continent in alphabetical order'''
    if "Asia" in locations:
        for i in locations['Asia']:
            for j in locations['Asia'][i]:
                s= s+j+" - "+i 
                result.append(s)
                s=""
        return result


# Note: Check for test cases to understand the output format.
locations = {'North America': {'USA': ['Mountain View']}}
list = [('Bangalore', 'India', 'Asia'),('Atlanta', 'USA','North America'),('Cairo','Egypt','Africa'),('Shanghai','China','Asia')]
for i in list:
    if i[2] in locations:
        if i[1] in locations[i[2]]:
            locations[i[2]][i[1]].append(i[0])
        else:
            locations[i[2]][i[1]] = [i[0]]
    else:
        locations[i[2]] = {i[1]:[i[0]]}

# print(locations)
# print(sortUSA(locations))
# print(alphaAsia(locations))

