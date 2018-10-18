def themeh(l):
#r = []
    c = 0
#t = []
#This checks to see if l is a list or not
    if type(l) != list:
        raise TypeError

#
    for element in l:# Checking the elements
        if type(element) == int:# Checking to see if said element is an actual number
            if element > 0:# Checking to see if the element is a poitive integer
                c += 1# Adds the number of positive variables to c
    return str(c) and list(c)


themeh ([5, -7, 4, -12, -26, 6])
