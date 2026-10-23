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
print("\nACTIVITY 2: Manual Chunking")
sentence = "The teacher explains the lesson in the classroom."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
tree = chunker.parse(tagged)
print("Sentence:", sentence)
print("POS Tags:", tagged)
print("Chunk Structure:", tree)
