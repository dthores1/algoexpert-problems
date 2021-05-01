def kmp(pat, text):
    text_length = len(text)
    pat_idx, txt_idx = 0, 0

    lps = compute_lps_array(pat)

    while txt_idx < text_length:
        if pat[pat_idx] == text[txt_idx]:
            pat_idx += 1
            txt_idx += 1

        if pat_idx == len(pat):
            print("Found pattern at index {0}".format(txt_idx - pat_idx))
            pat_idx = lps[pat_idx - 1]
        elif txt_idx < text_length and pat[pat_idx] != text[txt_idx]:
            if pat_idx != 0:
                pat_idx = lps[pat_idx - 1]
            else:
                txt_idx += 1

def compute_lps_array(pat):
    lps = [0] * len(pat)
    i, j = 0, 1
 
    while j < len(pat):
        if pat[i] == pat[j]:
            i += 1
            lps[j] = i
            j += 1
        else:
            if i != 0:
                i = lps[i-1]
            else:
                j += 1

    return lps