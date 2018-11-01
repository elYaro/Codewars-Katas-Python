'''
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should 
be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using "encode" in Python is considered cheating.
'''

import copy
import string

def rot13(message):
    print(message)
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_rot13 = "nopqrstuvwxyzabcdefghijklm"
    message2 = copy.deepcopy(message) 
    message2 = message2.lower()
    result = ""
    
    for i in range(0, len(message)):
        if message[i].isalpha():
            index_of_i = alpha.index(message2[i])
            next_letter_in_result = alpha_rot13[index_of_i]
            if message[i].islower():
                result += next_letter_in_result
            else:
                result += next_letter_in_result.upper()
        else:
            result += message[i]
    return result