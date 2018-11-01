'''
Define a function that removes duplicates from an array of numbers and returns it as a result.
The order of the sequence has to stay the same.
'''

def distinct(seq):
    final_list = [ ]
    for element in seq:
        if final_list.count(element) < 1:
            final_list.append(element)
    return final_list