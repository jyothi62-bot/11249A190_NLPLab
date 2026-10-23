import re
from collections import Counter
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
sentences = []
for line in corpus.split("\n"):
    words = re.findall(r"[a-z']+", line.lower())
    sentences.append(["<s>", "<s>"] + words + ["</s>"])
bigrams = Counter()
trigrams = Counter()
vocab = set()
for sentence in sentences:
    vocab.update(sentence)
    for i in range(len(sentence) - 2):
        bigrams[(sentence[i], sentence[i+1])] += 1
        trigrams[(sentence[i], sentence[i+1], sentence[i+2])] += 1
V = len(vocab)
def trigram_prob(w1, w2, w3):
    return (trigrams[(w1, w2, w3)] + 1) / (bigrams[(w1, w2)] + V)
print("Trigram\t\t\tCount\tProbability")
for (w1, w2, w3), count in trigrams.most_common(6):
    print(w1, w2, w3, "\t", count, "\t",
          round(trigram_prob(w1, w2, w3), 4))
def sentence_probability(sentence):
    words = re.findall(r"[a-z']+", sentence.lower())
    words = ["<s>", "<s>"] + words + ["</s>"]
    probability = 1
    for i in range(len(words) - 2):
        probability *= trigram_prob(
            words[i], words[i+1], words[i+2]
        )
    return probability
test = "the quick fox"
print("\nP('the quick fox') =", sentence_probability(test))