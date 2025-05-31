def inverted_index_builder(messages):
    inverted_index = {}
    for i, msg in enumerate(messages):
        words = set(msg.strip().split())  # Unique words only
        for word in words:
            if word not in inverted_index:
                inverted_index[word] = set()
            inverted_index[word].add(i)
    return inverted_index
