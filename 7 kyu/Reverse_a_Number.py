'''
Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)
Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

Examples
 123 ->  321
-456 -> -654
1000 ->    1
'''

def reverse_number(n):
    print(n)
    if n >= 0:
        return int(str(n)[::-1])
    else:
        return int(str(n)[:0:-1]) * -1