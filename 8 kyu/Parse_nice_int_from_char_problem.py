'''
Ask a small girl - "How old are you?". She always says strange things... Lets help her!
For correct answer program should return int from 0 to 9.
Assume test input string always valid and may look like "1 year old" or "5 years old", etc.. The first char is number only.
'''

# 2nd try - after refactor
def get_age(age):
    for i in age:
        if i.isdigit():
            return int(i)
        
# 1st try
def get_age(age):
     for element in age:
         if element.isdigit():
             return int(element)
    