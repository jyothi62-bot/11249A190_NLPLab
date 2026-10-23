import re
import random
from collections import Counter, defaultdict
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
model = defaultdict(Counter)
for line in corpus.split("\n"):
    words = ["<s>"] + re.findall(r"[a-z']+", line.lower()) + ["</s>"]
    for i in range(len(words) - 1):
        model[words[i]][words[i + 1]] += 1
def generate_sentence():
    word = "<s>"
    sentence = []
    for i in range(15):
        next_words = model[word]
        if not next_words:
            break
        words = list(next_words.keys())
        counts = list(next_words.values())
        word = random.choices(words, weights=counts)[0]
        if word == "</s>":
            break
        sentence.append(word)
    return " ".join(sentence)
random.seed(42)
for i in range(3):
    print("Sentence", i + 1, ":", generate_sentence())