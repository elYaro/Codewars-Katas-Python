'''
Write a function that takes an array/list of numbers and returns a number.

See the examples and try to guess the pattern:
even_odd([1,2,6,1,6,3,1,9,6]) => 393
even_odd([1,2,3]) => 5
even_odd([0,2,3]) => 3
even_odd([1,0,3]) => 3
even_odd([3,2])   => 6
'''

def even_odd(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[0]*arr[1]
    if len(arr) == 3:
        return arr[0] * arr[1] + arr[2]
    else:
        arr = [(arr[0] * arr[1] + arr[2])] + arr[3:] #      (arr[0] * arr[1] + arr[2]) + 
        return even_odd(arr)