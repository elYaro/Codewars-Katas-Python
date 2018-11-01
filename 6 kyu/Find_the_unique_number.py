'''
There is an array with some numbers. All numbers are equal except for one. Try to find it!

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance.
This is the first kata in series:
Find the unique number (this kata)
Find the unique string
Find The Unique
'''

# 2nd try - after refactor
def find_uniq(arr):
    arr.sort()
    return arr[0] if arr[0] != arr[1] else arr[-1]

# 1st try
def find_uniq(arr):
    arr.sort()
    if arr[0] != arr[1]:
        return arr[0]
    return arr[-1]