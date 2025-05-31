# def highlight_matches(text: str, pattern: str) -> str:
#     if not pattern:
#         return text

#     lower_text = text.lower()
#     lower_pattern = pattern.lower()

#     lps = [0] * len(lower_pattern)
#     i = 1
#     while i < len(lower_pattern):
#         if lower_pattern[i] == lower_pattern[length]:
#             length += 1
#             lps[i] = length
#             i += 1
#         else:
#             if length != 0:
#                 length = lps[length - 1]
#             else:
#                 lps[i] = 0
#                 i += 1

#     i = j = 0
#     match_starts = []
#     while i < len(lower_text):
#         if lower_pattern[j] == lower_text[i]:
#             i += 1
#             j += 1
#         if j == len(lower_pattern):
#             match_starts.append(i - j)
#             j = lps[j - 1]
#         elif i < len(lower_text) and lower_pattern[j] != lower_text[i]:
#             if j != 0:
#                 j = lps[j - 1]
#             else:
#                 i += 1

#     chars = list(text)
#     for start in reversed(match_starts):
#         end = start + len(pattern)
#         chars.insert(end, "</mark>")
#         chars.insert(start, '<mark style="color: black;">')

#     return ''.join(chars)


def highlight_matches(text : str, pattern : str) -> str:

    if not pattern:
        return text
    
    lower_pattern = pattern.lower()
    lower_text = text.lower()

    lps = [0] * len(lower_pattern)
    i = 0
    j = 1
    lps[0] = 0
    while (j < len(lower_pattern)):
        if (lower_pattern[j] == lower_pattern[i]) :
            lps[j] = i + 1
            j += 1
            i += 1
        else : 
            if i == 0:
                lps[j] = 0
                j += 1
            else:
                i = lps[i - 1]
    
    i = 0
    j = 0
    starting_indices = []
    while (i < len(lower_text) ) :
        if (lower_pattern[j] == lower_text[i]) :
            i += 1
            j += 1
            if (j == len(lower_pattern)) :
                starting_indices.append(i - j) 
                j = lps[j - 1]

        else:
            if (j == 0):
                i += 1
            else:
                j = lps[j - 1]
    
    chars = list(text)
    
    for start in reversed(starting_indices) :
        chars.insert(start+ len(lower_pattern),"</mark>")
        chars.insert(start,'<mark style=" color: black;">')
    
    return ''.join(chars)



         

    



    

