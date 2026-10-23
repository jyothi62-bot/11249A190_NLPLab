import re
from collections import Counter
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
sentences = []
for line in corpus.split("\n"):
    words = re.findall(r"[a-z']+", line.lower())
    sentences.append(["<s>"] + words + ["</s>"])
unigrams = Counter()
bigrams = Counter()
vocab = set()
for sentence in sentences:
    unigrams.update(sentence[:-1])
    vocab.update(sentence)
    for i in range(len(sentence) - 1):
        bigrams[(sentence[i], sentence[i + 1])] += 1
V = len(vocab)
def bigram_prob(w1, w2):
    return (bigrams[(w1, w2)] + 1) / (unigrams[w1] + V)
print("Bigram\t\tCount\tProbability")
print("-" * 40)
for (w1, w2), count in bigrams.most_common(8):
    print(
        w1, w2,
        "\t", count,
        "\t", round(bigram_prob(w1, w2), 4)
    )
def sentence_probability(sentence):
    words = re.findall(r"[a-z']+", sentence.lower())
    words = ["<s>"] + words + ["</s>"]
    probability = 1
    for i in range(len(words) - 1):
        probability *= bigram_prob(words[i], words[i + 1])
    return probability
test = "the fox runs"
print("\nP('the fox runs') =",
      round(sentence_probability(test), 10))