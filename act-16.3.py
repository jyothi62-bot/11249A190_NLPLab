import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
grammar = r"""
    NP: {<DT>?<RB.*>*<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""
chunker = nltk.RegexpParser(grammar)
print("\nACTIVITY 3: Annotate a Sentence")
sentence = "The young researcher develops an AI model."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
tree = chunker.parse(tagged)
print("Sentence:", sentence)
print("POS-Tagged Sequence:", tagged)
print("Noun Phrase Bracketing:", tree)
