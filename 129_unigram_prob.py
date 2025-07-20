def unigram_probability(corpus: str, word: str) -> float:
    # Your code here
    tokens = corpus.lower().split() # convert the string to lowercase; should return a list
    if len(tokens) == 0:
        return 0

    word_prob = tokens.count(word.lower()) / len(tokens) # searching for the token (also in lowercase among the tokens)
    return round(word_prob, 4)