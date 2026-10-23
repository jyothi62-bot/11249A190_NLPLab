import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
def pos_tag_sentence(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(tokens)

    print("\nSentence:", sentence)
    print("Word\tPOS Tag")
    print("-" * 25)
    for word, tag in tagged_words:
        print(f"{word}\t{tag}")
print("ACTIVITY 1")
pos_tag_sentence("Ravi plays cricket every evening.")