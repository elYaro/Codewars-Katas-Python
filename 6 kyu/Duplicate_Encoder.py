'''
The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.

Examples:
"din" => "((("
"recede" => "()()()"
"Success" => ")())())"
"(( @" => "))(("

Notes:
Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is actually the expected result, 
not the input! (these languages are locked so that's not possible to correct it).
'''

import copy
def duplicate_encode(word): 
    word = word.lower()
    word2 = copy.deepcopy(word)
    word3 = ""
    for i in word:
        how_many_times_in_word = word.count(i)
        if how_many_times_in_word > 1:
            word2 = word2.replace(i, ")", 1)
            word3 += ")"
        else:
            word2 = word2.replace(i, "(" , 1)
            word3 += "("
    return word3