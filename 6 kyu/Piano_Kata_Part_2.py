'''
You will be given an vector of string(s). You must sort it alphabetically (case-sensitive!!) and then return the first value.
The returned value must be a string, and have "***" between each of its letters.
You should not remove or add elements from/to the array.
'''

def which_note(key_press_count):
    keyboard = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
    return keyboard[(key_press_count - 1) % 88 % 12]