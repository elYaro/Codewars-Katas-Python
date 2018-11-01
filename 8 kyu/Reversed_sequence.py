'''
Get the number n (n>0) to return the reversed sequence from n to 1.
Example : n=5 >> [5,4,3,2,1]
'''

# 2nd try - after refacotr
def reverse_seq(n):
    return list(range(n,0,-1))

# 1st try
def reverse_seq(n):
    st = list()
    for i in range (n,0,-1):
        st.append(i)
    return st