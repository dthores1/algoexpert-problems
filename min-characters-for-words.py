"""
    Write a function that takes in an array of words and returns the smallest
    array of characters needed to form all of the words. The characters don't need
    to be in any particular order.

    For example, the characters ["y", "r", "o", "u"] are needed to
    form the words ["your", "you", "or", "yo"].

    Note: the input words won't contain any spaces; however, they might contain
    punctuation and/or special characters.

    Example:
        words = ["this", "that", "did", "deed", "them!", "a"]

        Output:
            ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
"""
def minimumCharactersForWords(words):
    result = []
    dict = get_char_dict(words)

    for x in dict:
        for i in range(0, dict[x]):
            result.append(x)

    return result


def get_char_dict(words):
    dict = {}
    for word in words:

        dict_for_word = {}

        for c in word:
            if c in dict_for_word:
                dict_for_word[c] = dict_for_word[c] + 1
            else:
                dict_for_word[c] = 1

        for c in dict_for_word:
            if c not in dict or dict[c] < dict_for_word[c]:
                dict[c] = dict_for_word[c]

    return dict        


print(minimumCharactersForWords(["this", "that", "did", "deed", "them", "they"]))