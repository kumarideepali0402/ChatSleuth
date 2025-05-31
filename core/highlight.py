def highlight_matches(text: str, pattern: str) -> str:
    if not pattern:
        return text

    # Case-insensitive match
    lower_text = text.lower()
    lower_pattern = pattern.lower()

    # Build LPS array for KMP
    lps = [0] * len(lower_pattern)
    length = 0  # length of the previous longest prefix suffix
    i = 1
    while i < len(lower_pattern):
        if lower_pattern[i] == lower_pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    # Find all match indices using KMP
    i = j = 0
    match_starts = []
    while i < len(lower_text):
        if lower_pattern[j] == lower_text[i]:
            i += 1
            j += 1
        if j == len(lower_pattern):
            match_starts.append(i - j)
            j = lps[j - 1]
        elif i < len(lower_text) and lower_pattern[j] != lower_text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    # Highlight all matches (insert tags in reverse to not mess up positions)
    chars = list(text)
    for start in reversed(match_starts):
        end = start + len(pattern)
        chars.insert(end, "</mark>")
        chars.insert(start, '<mark style="color: black;">')

    return ''.join(chars)
