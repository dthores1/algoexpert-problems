"""
    Write a function that takes in a non-empty string and that returns a boolean
    representing whether the string is a palindrome.

    A palindrome is defined as a string that's written the same forward and
    backward. Note that single-character strings are palindromes.

    Example:
        string = "abcdcba"

        Output: true
"""
# Stack Solution
# O(n) time | O(n) space
def is_palindrome(string):
    is_even = len(string) % 2 == 0
    midpoint = len(string) // 2
    stack = []

    for idx, char in enumerate(string):
        if idx < midpoint:
            stack.append(char)
        elif idx != midpoint or is_even:
            if char != stack.pop():
                return False

    return True

# Deque solution
# O(n) time | O(n) space
def is_palindrome(string):
    deque = list(string)

    while len(deque) > 1:
        if deque.pop(0) != deque.pop():
            return False

    return True

# Pointers solution
# O(n) time | O(1) space
def is_palindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1

    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False

        leftIdx += 1
        rightIdx -= 1

    return True

# Recursive Solution
# O(n) time | O(n) space
def is_palindrome(string, i=0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and is_palindrome(string, i + 1)

assert is_palindrome("abcdcba")
assert is_palindrome("kayak")
assert is_palindrome("a")
assert is_palindrome("bbbbb")
assert is_palindrome("cccccc")
assert not is_palindrome("kayaks")