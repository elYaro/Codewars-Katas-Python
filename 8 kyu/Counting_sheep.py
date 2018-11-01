'''
Consider an array of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined
'''

def count_sheeps(arrayOfSheeps):
  # TODO May the force be with you
    suma=0
    for i in arrayOfSheeps:
        if i==True:
            suma=suma+i
    return suma