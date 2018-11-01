'''
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot seperating them.
It should look like this:
Sam Harris => S.H
Patrick Feeney => P.F
'''

# 2nd try - after refactor 
def abbrevName(name): 
    a = name.split()
    return "{0:s}.{1:s}".format(a[0][0].upper(), a[1][0].upper())


# 1st try 
def abbrevName(name):
    a = (name.split())  
    return "{}.{}".format(a[0][0].upper(), a[1][0].upper())