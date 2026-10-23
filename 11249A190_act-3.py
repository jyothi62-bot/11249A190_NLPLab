import re
from collections import Counter
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
sentences = []
for line in corpus.split("\n"):
    words = re.findall(r"[a-z']+", line.lower())
    sentences.append(["<s>", "<s>", "<s>"] + words + ["</s>"])
quadgrams = Counter()
trigrams = Counter()
for sentence in sentences:
    for i in range(len(sentence) - 3):
        trigrams[
            (sentence[i], sentence[i+1], sentence[i+2])
        ] += 1

        quadgrams[
            (sentence[i], sentence[i+1],
             sentence[i+2], sentence[i+3])
        ] += 1
V = len(set(sum(sentences, [])))
def quadgram_prob(w1, w2, w3, w4):
    return (
        quadgrams[(w1, w2, w3, w4)] + 1
    ) / (
        trigrams[(w1, w2, w3)] + V
    )
print("Quadgram\t\tCount\tProbability")
for quadgram, count in quadgrams.most_common(10):
    print(quadgram, "\t", count,
          "\t", round(quadgram_prob(*quadgram), 4))