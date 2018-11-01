'''
You have been recruited by an unknown organization for your cipher encrypting/decrypting skills.
Being new to the organization they decide to test your skills.
Your first test is to write an algorithm that encrypts the given string in the following steps.

The first step of the encryption is a standard ROT13 cipher. This is a special case of the caesar cipher where the letter is encrypted with its key that is 
thirteen letters down the alphabet,
i.e. A => N, B => O, C => P, etc..
Part two of the encryption is to take the ROT13 output and replace each letter with its exact opposite. A => Z, B => Y, C => X.
The return value of this should be the encrypted message.
Do not worry about capitalization or punctuation. All encrypted messages should be lower case and punctuation free.
As an example, the string "welcome to our organization" should return "qibkyai ty ysv yvgmzenmteyz".

Good luck, and congratulations on the new position.
'''

import copy

def encrypter(message):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_rot13 = "nopqrstuvwxyzabcdefghijklm"
    alpha_rot13_part2 = "mlkjihgfedcbazyxwvutsrqpon"
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
    message = result
    print(message)
    message2 = copy.deepcopy(message) 
    print(message2)
    message2 = message2.lower()
    print(message2)
    result = ""
    print(result)
    for i in range(0, len(message)):
        if message[i].isalpha():
            index_of_i = alpha_rot13.index(message2[i])
            next_letter_in_result = alpha_rot13_part2[index_of_i]
            if message[i].islower():
                result += next_letter_in_result
            else:
                result += next_letter_in_result.upper()
        else:
            result += message[i]
    return result