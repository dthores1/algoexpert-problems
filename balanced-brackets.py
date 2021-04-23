"""
    Write a function that takes in a string made up of brackets ((, [, {, ), ], and }) 
    and other optional characters. The function should return a boolean representing 
    whether the string is balanced with regards to brackets.

    A string is said to be balanced if it has as many opening brackets of a
    certain type as it has closing brackets of that type and if no bracket is
    unmatched. Note that an opening bracket can't match a corresponding closing
    bracket that comes before it, and similarly, a closing bracket can't match a
    corresponding opening bracket that comes after it. Also, brackets can't
    overlap each other as in [(])

    Example:
    string =  = "([])(){}(())()()"

    Output: True
"""
def balancedBrackets(string):
    balanced = True
    stack = []
    opening_chars = "({["
    closing_chars = ")}]"

    for char in string:
        if char in opening_chars:
            stack.append(char)
        elif char in closing_chars:
            if len(stack):
                opening_char = stack.pop()
                if opening_chars.index(opening_char) != closing_chars.index(char):
                    balanced = False
                    break
            else:
                balanced = False

    return len(stack) == 0 and balanced



print(balancedBrackets("([])(){}(())()()"))