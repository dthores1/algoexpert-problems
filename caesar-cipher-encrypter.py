"""
    Given a non-empty string of lowercase letters and a non-negative integer
    representing a key, write a function that returns a new string obtained by
    shifting every letter in the input string by k positions in the alphabet,
    where k is the key.


    Note that letters should "wrap" around the alphabet; in other words, the
    letter "z" shifted by one returns the letter "a".

    Example:
        string = "xyz"
        key = 2

        Output:
            "zab"
"""
def caesarCipherEncryptor(string, key):
    chars = list("abcdefghijklmnopqrstuvwxyz")
    result = []
    
    for char in string:
        result.append(shift_char(char, key, chars))

    return "".join(result)

def shift_char(char, key, chars):
    if len(chars) - 1 > chars.index(char) + key:
        return chars[chars.index(char) + key]
    else:
        if key < len(chars):
            shift_front = (chars.index(char) + key) - len(chars)
        else:
            shift_front = (key % len(chars)) + chars.index(char)
        return chars[shift_front]