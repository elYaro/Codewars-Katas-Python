'''
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
'''

def fake_bin(x):
    result = ""
    for i in x:
        if int(i) < 5:
            result += "0" 
        else:
            result += "1"
    return result
    
    # return x.replace(i, 0) for i in x if i < 5 else x.replace(i, 1) for i in x if i >= 5