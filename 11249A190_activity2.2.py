from collections import Counter
text = input("Enter a sentence: ").lower().split()
unigram_counts = Counter(text)
total_words = len(text)
print("\nUnigram Probabilities:")
for word, count in unigram_counts.items():
    probability = count / total_words
    print(f"P({word}) = {count}/{total_words} = {probability:.4f}")
bigrams = [(text[i], text[i + 1]) for i in range(len(text) - 1)]
bigram_counts = Counter(bigrams)

print("\nBigram Probabilities:")
for (w1, w2), count in bigram_counts.items():
    probability = count / unigram_counts[w1]
    print(f"P({w2}|{w1}) = {count}/{unigram_counts[w1]} = {probability:.4f}")