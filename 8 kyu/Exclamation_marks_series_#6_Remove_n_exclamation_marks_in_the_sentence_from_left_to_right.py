'''
Description:
Remove n exclamation marks in the sentence from left to right. n is positive integer.

Examples
remove("Hi!",1) === "Hi"
remove("Hi!",100) === "Hi"
remove("Hi!!!",1) === "Hi!!"
remove("Hi!!!",100) === "Hi"
remove("!Hi",1) === "Hi"
remove("!Hi!",1) === "Hi!"
remove("!Hi!",100) === "Hi"
remove("!!!Hi !!hi!!! !hi",1) === "!!Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",3) === "Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",5) === "Hi hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",100) === "Hi hi hi"

Note
Please don't post issue about difficulty or duplicate.
'''

# 3rd try - after another refactor
def remove(s, n):
    return s.replace("!","",n)

# 2nd try - after refactor
def remove(s, n):
    s_list, i = list(s), 1
    while "!" in s_list and i <=n:
        s_list.remove("!")
        i+=1
    return "".join(s_list) 

# 1st try
def remove(s, n):
    s_list = list(s)
    i = 1
    while "!" in s_list and i <=n:
        s_list.remove("!")
        i+=1
    return "".join(s_list)