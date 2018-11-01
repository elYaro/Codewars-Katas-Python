'''
You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

12 ==> 21
513 ==> 531
2017 ==> 2071
If no bigger number can be composed using those digits, return -1:

9 ==> -1
111 ==> -1
531 ==> -1
'''

def next_bigger(n):
    
    sor_str_n = sorted(str(n))
    if str(n) == ''.join(sor_str_n)[::-1]:
        return -1
    
    i = n
    while True:
        i += 1
        if sorted(str(i)) == sor_str_n:
            return i