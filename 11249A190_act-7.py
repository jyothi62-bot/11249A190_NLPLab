import re
training_text = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
test_sentence = "the fox flies over the moon"
training_words = set(
    re.findall(r"[a-z']+", training_text.lower())
)

test_words = re.findall(
    r"[a-z']+", test_sentence.lower()
)

oov_words = []
for word in test_words:
    if word not in training_words:
        oov_words.append(word)
oov_rate = len(oov_words) / len(test_words) * 100
print("Test words:", test_words)
print("OOV words:", oov_words)
print("OOV Rate:", round(oov_rate, 2), "%")