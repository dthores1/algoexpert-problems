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