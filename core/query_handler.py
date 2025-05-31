def word_search(query, inverted_index) :
    words = query.split()
    result = inverted_index.get(words[0], set())

    for word in words[1:]:
        result &= inverted_index.get(word, set())
    return result



