"""
    Write a function that takes in a string and returns its longest substring without 
    duplicate characters.

    You can assume that there will only be one longest substring without duplication.
    
    Example:
        string = "clementisacap"

    Output:
        "mentisac"
"""
def longestSubstringWithoutDuplication(s):
    longest_substring = [0, 0]
    start, end = 0, 0

    while end < len(s):
        char = s[end]

        if char not in s[start:end]:
            if (end - start) > (longest_substring[1] - longest_substring[0]):
                longest_substring = [start, end]
        else:
            # increment start pointer
            while start <= end and char in s[start:end]:
                start += 1
                if (end - start) > (longest_substring[1] - longest_substring[0]):
                    longest_substring = [start, end]                
        end += 1

    return "".join(s[longest_substring[0]:longest_substring[1]+1])

assert longestSubstringWithoutDuplication("abcad") == "bcad"
assert longestSubstringWithoutDuplication("clementisacap") == "mentisac"
assert longestSubstringWithoutDuplication("bbbbb") == "b"