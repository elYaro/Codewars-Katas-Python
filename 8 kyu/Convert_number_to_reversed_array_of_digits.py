'''
Convert number to reversed array of digits
Given a random number:
C#: long;
C++: unsigned long;
You have to return the digits of this number within an array in reverse order.

Example:
348597 => [7,9,5,8,4,3]
'''

def digitize(n):
    nstr = str(n)
    l=[int(nstr[i]) for i in range(len(nstr)-1,-1,-1)]
    return l