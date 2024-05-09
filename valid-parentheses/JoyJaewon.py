'''
input: string - containing only parentheses
output: boolean - check if the string is valid

test cases
"()" == true
"()[]{}" == true
"(]"  == false
"" == true 

Approahch:
use stack to track opening brackets
1. Initialize the stack
2. Map the closing brackets to their corresponding opening brackets using dictionary
3. Iterate through each string
    3-1. if it's the opening bracket, push it to the stack
    3-2. if it's the closing bracket, pop the stack and check if it matches
4. return not stack
TC: O(N), SC: O(N)
'''

def isValid(s):
    stack = []
    bracket_pair = {')' : '(', '}' : '{', ']' : '['}
    
    for char in s:
        if char in bracket_pair.values():
            stack.append(char)
        else:
            if not stack or stack.pop() != bracket_pair[char]:
                return False
    
    return not stack


#TC: O(N), SC: O(N)

#Normal case
print(isValid("()") == True)
print(isValid("()[]{}") == True)
print(isValid("(]") == False)

#Edge case
print(isValid("") == True)

