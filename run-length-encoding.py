"""
    Write a function that takes in a non-empty string and returns its run-length
    encoding.

    From Wikipedia, "run-length encoding is a form of lossless data compression in
    which runs of data are stored as a single data value and count, rather than as
    the original run." For this problem, a run of data is any sequence of
    consecutive, identical characters. So the run "AAA" would be run-length-encoded 
    as "3A".

    To make things more complicated, however, the input string can contains all sorts 
    of special characters, including numbers. And since encoded data must be decodable,
    this means that we can't naively run-length-encode long runs. For example, the run
    "AAAAAAAAAAAA" (12 A's), can't naively be encoded as "12A", since this string can 
    be decoded as either "AAAAAAAAAAAA" or "1AA". Thus, long runs (runs of 10 or more
    characters) should be encoded in a split fashion; the aforementioned run should be 
    encoded as "9A3A".

    Example: 
        string = "AAAAAAAAAAAABBCCCCDD"

        Output:
            "9A4A2B4C2D"
"""

def runLengthEncoding(string):
    results_array = []
    last_char = None
    char_count = 0

    for char in string:
        if (last_char is not None and last_char != char) or char_count == 9:
            results_array.append(str(char_count) + last_char)
            char_count = 0

        char_count += 1
        last_char = char
    
    # Don't forget the last character
    results_array.append(str(char_count) + last_char)
    return "".join(results_array)

#print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))
print(runLengthEncoding("aA"))