'''
Your job is to create a calculator which evaluates expressions in Reverse Polish notation.
For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.
For your convenience, the input is formatted such that a space is provided between every token.
Empty expression should evaluate to 0.
Valid operations are +, -, *, /.
You may assume that there won't be exceptional situations (like stack underflow or division by zero).
'''

import operator


def calc(expr):
    list_actions_available={"+":operator.add,
                        "-":operator.sub,
                        "*":operator.mul,
                        "/":operator.truediv}
    data = []  
    for element in expr.split():
        if element in list_actions_available:
            action = list_actions_available[element]
            second = data.pop()
            first = data.pop() 
            result = action((first),int(second))
            data.append(result)
            
        else:
            data.append(float(element))
    if data:
        return data[-1]
    else:
        return 0