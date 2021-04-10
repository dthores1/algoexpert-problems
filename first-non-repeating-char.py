"""
    Write a function that takes in a string of lowercase English-alphabet letters
    and returns the index of the string's first non-repeating character.

    The first non-repeating character is the first character in a string that
    occurs only once.

    If the input string doesn't have any non-repeating characters, your function
    should return -1.

    Example:
        string = "abcdcaf"

        Output:
            1
"""
def firstNonRepeatingCharacter(string):
    found_chars = {}
    for char in string:
        found_chars[char] = found_chars.get(char, 0) + 1

    for idx in range(len(string)):
        if found_chars[string[idx]] is 1:
            return idx

    return -1