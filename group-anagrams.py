"""
    Write a function that takes in an array of strings and groups anagrams together.


    Anagrams are strings made up of exactly the same letters, where order doesn't
    matter. For example, "cinema" and "iceman" are anagrams; similarly, "foo" and
    "ofo" are anagrams.

    Your function should return a list of anagrams in no particular order.

    Example:
        words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

        Output:
            [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
"""
# Not a great solution; lengthy and some parts not DRY
def groupAnagrams(words):
    words = sorted(words, key=len)
    result_indices_by_word_len = {}
    results = []

    last_word_len = None

    for word in words:
        word_len = len(word)
        if last_word_len != word_len:
            last_word_len = word_len
            results.append([word])
            result_indices_by_word_len[word_len] = [len(results) - 1]
            continue

        if word_len in result_indices_by_word_len:
            found_anagram = False
            for i in result_indices_by_word_len[word_len]:
                if is_anagram(results[i][0], word):
                    arr = results[i]
                    arr.append(word)
                    results[i] = arr
                    found_anagram = True
                    break

            if not found_anagram:
                results.append([word])
            
                arr = result_indices_by_word_len.get(word_len, [])
                arr.append(len(results)-1)
                result_indices_by_word_len[word_len] = arr
        else:
            results.append([word])
            
            arr = result_indices_by_word_len.get(word_len, [])
            arr.append(len(results)-1)
            result_indices_by_word_len[word_len] = arr

        last_word_len = word_len

    return results

def is_anagram(word1, word2):
    letters = {}
    for char in word1:
        char_count = letters.get(char, 0)
        char_count += 1
        letters[char] = char_count

    for char in word2:
        if char not in letters:
            return False

        char_count = letters[char] - 1

        if char_count is 0:
            del letters[char]
        else:
            letters[char] = char_count

    return True



def group_anagrams(words):
    anagrams = {}

    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())