def count_frequency(word):
    with open('texts/text.txt', 'r') as f:
        text = f.read()
        words = text.split()

        word_frequency = dict()
        for w in words:
            word_frequency[w] = words.count(w)
        
    return word_frequency.get(word)