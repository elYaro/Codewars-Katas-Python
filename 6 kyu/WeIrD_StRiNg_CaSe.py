'''
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, 
and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character 
should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be 
separated by a single space(' ').

Examples:
toWeirdCase( "String" );//=> returns "StRiNg"
toWeirdCase( "Weird string case" );//=> returns "WeIrD StRiNg CaSe"
'''

# 2nd try - after refactor
def to_weird_case(string):
    string = list(string)
    i = 0
    while i < len(string):
        if i % 2 == 0:
            if string[i] != " ": 
                string[i] = string[i].upper()
            else: string.insert(i+1, " ")    
        else: string[i] = string[i].lower()
        i += 1      
    string = "".join(string)
    return(string.replace("  ", " "))

# 1st try
    def to_weird_case(string):
    if len(string) == 1: return string.upper()
    else: string = list(string)        
    i = 0
    while i < len(string):
        if i % 2 == 0:
            if string[i] != " ": 
                string[i] = string[i].upper()
            else: string.insert(i+1, " ")    
        else: string[i] = string[i].lower()
        i += 1      
    string = "".join(string)
    return(string.replace("  ", " "))