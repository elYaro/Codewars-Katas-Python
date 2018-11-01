'''
Write a function called repeatStr which repeats the given string string exactly n times.
repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"
'''

# 3rd try - after refactor again
def repeat_str(repeat, string):
    return string*repeat

# 2nd try - after refactor
def repeat_str(repeat, string):
    return repeat*string

# 1st try
def repeat_str(repeat, string):
    return ''.join(string)*repeat