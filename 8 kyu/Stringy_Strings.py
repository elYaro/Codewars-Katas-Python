'''
write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.
the string should start with a 1.
a string with size 6 should return :'101010'.
with size 4 should return : '1010'.
with size 12 should return : '101010101010'.
The size will always be positive and will only use whole numbers.
'''

# 2nd try - after refactor
def stringy(size):
    return "10" * int(size // 2) + "1" * int(size % 2)


# 1st try
def stringy(size):
    if size == 1:
        return "1"
    elif size % 2 == 0:
        return ("10" * int(size // 2))
    else:
        return ("10" * int(size // 2) + "1")