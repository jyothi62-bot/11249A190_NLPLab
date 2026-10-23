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
print("\nACTIVITY 2: Extended Noun Phrase Rule")
sentence = "The students read their textbooks."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
tree = chunker.parse(tagged)
print("Sentence:", sentence)
print("Updated Grammar:")
print(grammar)
print("POS Tags:", tagged)
print("Chunk Tree:", tree)
