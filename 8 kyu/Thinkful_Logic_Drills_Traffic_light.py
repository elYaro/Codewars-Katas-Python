'''
You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.
Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light 
should change to.
For example, update_light('green') should return 'yellow'.
'''

# 2nd try - after refactor
def update_light(current):
    combinations = {"green" : "yellow", "yellow" : "red", "red" : "green"}
    return combinations[current]

# 1st try
def update_light(current):
    colors_lst = ["green", "yellow", "red"]
    index_of_current = colors_lst.index(current) 
    if current == "red":
        return "green"
    else:
        return colors_lst[index_of_current +1]
 