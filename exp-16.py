import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentence = "The boy can play in the beautiful garden."
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)
print("POS TAGGING")
print(tagged_words)
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""
chunk_parser = nltk.RegexpParser(grammar)
chunk_tree = chunk_parser.parse(tagged_words)
print("\nCHUNKING RESULT")
print(chunk_tree)
