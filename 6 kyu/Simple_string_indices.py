'''
In this Kata, you will be given a string with brackets and an index of an opening bracket and your task will be to return the index of the matching closing bracket. Both the input and returned index are 0-based except in Fortran where it is 1-based. An opening brace will always have a closing brace. Return -1 if there is no answer (Haskell return Nothing, Fortran: return 0)

Examples
solve("((1)23(45))(aB)", 0) = 10 -- the opening brace at index 0 matches the closing brace at index 10
solve("((1)23(45))(aB)", 1) = 3 
solve("((1)23(45))(aB)", 2) = -1 -- there is no opening bracket at index 2, so return -1
solve("((1)23(45))(aB)", 6) = 9
solve("((1)23(45))(aB)", 11) = 14
solve("((>)|?(*'))(yZ)", 11) = 14

Input will consist of letters, numbers and special characters, but no spaces. The only brackets will be ( and ).
More examples in the test cases.
Good luck!
'''

def solve(st, idx):
    answer = -1
    if st[idx] == "(":
        while len(st) >= idx: 
            if st[idx+1] == "(": answer -= 1 
            elif st[idx+1] == ")": answer += 1
            if answer == 0: return idx+1
            idx += 1
    return -1