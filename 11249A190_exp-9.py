from collections import Counter
import re
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
words = re.findall(r"[a-z']+", corpus.lower())
counts = Counter(words)
total = len(words)
print("Word\tCount\tProbability")
for word, count in counts.items():
    print(word, "\t", count, "\t", round(count / total, 4))
word = "fox"
probability = counts[word] / total
print("\nP('fox') =", round(probability, 4))