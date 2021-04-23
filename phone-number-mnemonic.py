"""
    Given an inputted number, return all the possible combinations of letters/numbers
    from a phone numbers keypad. 1 and 0 are not represented by any letters. 

    Example: 
        phoneNumber = "1905"

        Output: ['1w0j', '1w0k', '1w0l', '1x0j', '1x0k', '1x0l', '1y0j', '1y0k', '1y0l', '1z0j', '1z0k', '1z0l']
"""
def phoneNumberMnemonics(phoneNumber):
    options = []
    make_options(0, list(phoneNumber), list(phoneNumber), options)
    return options

def make_options(idx, phoneNumber, currentOne, options):
    if idx == len(phoneNumber):
        options.append("".join(currentOne))
        return

    if phoneNumber[idx] not in phone_map:
        make_options(idx + 1, phoneNumber, currentOne, options)
    else:
        for this_char in phone_map.get(phoneNumber[idx]):
            currentOne[idx] = this_char
            make_options(idx + 1, phoneNumber, currentOne, options)

phone_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

print(phoneNumberMnemonics("1905"))