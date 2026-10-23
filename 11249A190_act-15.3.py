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
print("\nACTIVITY 3")
pos_tag_sentence("I read a book.")
pos_tag_sentence("Please book a ticket.")
pos_tag_sentence("Children play football.")
pos_tag_sentence("We watched a play.")
