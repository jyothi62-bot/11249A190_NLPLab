import re
from collections import Counter
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
words = re.findall(r"[a-z']+", corpus.lower())
unigrams = Counter(words)
bigrams = Counter()
for i in range(len(words) - 1):
    bigrams[(words[i], words[i + 1])] += 1
matrix = {}
for w1 in unigrams:
    matrix[w1] = {}
    for w2 in unigrams:
        count = bigrams[(w1, w2)]
        matrix[w1][w2] = count / unigrams[w1]
vocab = list(unigrams.keys())
print("Bigram Probability Matrix")
print("\t" + "\t".join(vocab[:10]))
for w1 in vocab[:10]:
    print(w1, end="\t")
    for w2 in vocab[:10]:
        print(round(matrix[w1][w2], 2), end="\t")
    print()