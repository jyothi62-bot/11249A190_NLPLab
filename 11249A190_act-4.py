import nltk
nltk.download("gutenberg")
import re
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
from collections import Counter
text = gutenberg.raw("austen-emma.txt")
words = re.findall(r"[a-z']+", text.lower())
words = words[:5000]
print("Total words:", len(words))
fdist = FreqDist(words)
print("\nTop 10 Unigrams:")
for word, count in fdist.most_common(10):
    print(word, count, round(count / len(words), 4))
bigrams = Counter()
for i in range(len(words) - 1):
    bigrams[(words[i], words[i+1])] += 1
print("\nTop 10 Bigrams:")
for bigram, count in bigrams.most_common(10):
    print(bigram, count)
trigrams = Counter()
for i in range(len(words) - 2):
    trigrams[
        (words[i], words[i+1], words[i+2])
    ] += 1
print("\nTop 10 Trigrams:")
for trigram, count in trigrams.most_common(10):
    print(trigram, count)