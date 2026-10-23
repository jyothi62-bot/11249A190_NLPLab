import re
from nltk.probability import FreqDist
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
words = re.findall(r"[a-z']+", corpus.lower())
fdist = FreqDist(words)
N = len(words)
print("Word\tCount\tProbability")
print("-" * 30)
for word, count in fdist.items():
    probability = count / N
    print(word, "\t", count, "\t", round(probability, 4))
print("\nP(fox) =", round(fdist["fox"] / N, 4))