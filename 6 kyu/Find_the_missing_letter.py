'''
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:
['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)
'''

def find_missing_letter(chars):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    start = alpha.index(chars[0].lower())
    for letter in chars:
        if letter.lower() == alpha[start]: start += 1
        elif chars[0].islower(): return alpha[start].lower()
        else: return alpha[start].upper()