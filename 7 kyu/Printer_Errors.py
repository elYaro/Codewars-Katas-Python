'''
In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity,
are named with letters from a to m.
The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning 
that the printer used three times col  or a, four times color b, one time color h then one time color a...
Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm.
You have to write a function printer_error which given a string will output the error rate of the printer as a string representing 
a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.
The string has a length greater or equal to one and contains only letters from ato z.
'''

def printer_error(s):
    colors = ("abcdefghijklm")
    error_count = 0
    label_len = len(s)
    for char in s:
        if char not in colors:
            error_count += 1
    return "{0}/{1}".format(error_count, label_len)