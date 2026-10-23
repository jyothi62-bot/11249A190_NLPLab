import re
from collections import Counter
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
words = re.findall(r"[a-z']+", corpus.lower())
unigrams = Counter(words)
bigrams = Counter()
for i in range(len(words) - 1):
    bigrams[(words[i], words[i+1])] += 1
V = len(unigrams)
def bigram_probability(w1, w2, k):
    return (
        bigrams[(w1, w2)] + k
    ) / (
        unigrams[w1] + k * V
    )
w1 = "the"
w2 = "fox"
for k in [0.01,0.1, 0.5, 1, 2]:
    p = bigram_probability(w1, w2, k)
    print("k =", k, "Probability =", round(p, 4))