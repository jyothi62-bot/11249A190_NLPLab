import re
import random
from collections import defaultdict, Counter

corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""

words = re.findall(r"[a-z']+", corpus.lower())

# Bigram model
bigram_model = defaultdict(Counter)

for i in range(len(words) - 1):
    bigram_model[words[i]][words[i+1]] += 1


# Trigram model
trigram_model = defaultdict(Counter)

for i in range(len(words) - 2):
    key = (words[i], words[i+1])
    trigram_model[key][words[i+2]] += 1


# Generate using bigram
def generate_bigram():
    word = "the"
    result = [word]

    for i in range(10):
        next_words = bigram_model[word]

        if not next_words:
            break

        word = random.choice(list(next_words.keys()))
        result.append(word)

    return " ".join(result)


# Generate using trigram
def generate_trigram():
    w1 = "the"
    w2 = "quick"

    result = [w1, w2]

    for i in range(8):
        next_words = trigram_model[(w1, w2)]

        if not next_words:
            break

        w3 = random.choice(list(next_words.keys()))

        result.append(w3)

        w1 = w2
        w2 = w3

    return " ".join(result)


print("Bigram:")
print(generate_bigram())

print("\nTrigram:")
print(generate_trigram())