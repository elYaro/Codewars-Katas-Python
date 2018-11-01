'''
Given an array containing only integers, add all the elements and return the binary equivalent of that sum.
If the array contains any non-integer element (e.g. an object, a float, a string and so on), return false.
Note: The sum of an empty array is zero.
arr2bin([1,2]) == '11'
arr2bin([1,2,'a']) == false
'''

def arr2bin(arr):
    print(arr)
    dec_sum = 0
    for i in arr:
        if str(i) == "True":
            return False
        else:
            try:
                dec_sum += i
            except:
                return False
    return bin(dec_sum) [2:]