import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
grammar = r"""
    NP: {<DT|PRP\$>?<RB.*>*<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""
chunker = nltk.RegexpParser(grammar)
print("\nACTIVITY 3: Compare Grammar Rules")
sentence = "The student reads a book in the library."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
np_grammar = r"""
    NP: {<DT|PRP\$>?<RB.*>*<JJ.*>*<NN.*>+}
"""
np_chunker = nltk.RegexpParser(np_grammar)
np_tree = np_chunker.parse(tagged)
print("NP-only Chunk Tree:")
print(np_tree)
full_tree = chunker.parse(tagged)
print("\nNP + VP + PP Chunk Tree:")
print(full_tree)
