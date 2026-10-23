import re
import matplotlib.pyplot as plt
from collections import Counter
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
words = re.findall(r"[a-z']+", corpus.lower())
counts = Counter(words)
top_words = counts.most_common(10)
words = [x[0] for x in top_words]
frequencies = [x[1] for x in top_words]
plt.bar(words, frequencies)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 10 Unigrams")
plt.xticks(rotation=45)
plt.show()