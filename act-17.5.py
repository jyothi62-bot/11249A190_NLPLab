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
print("\nACTIVITY 5: Error Analysis")
sentence = "The very intelligent student is reading a book."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
tree = chunker.parse(tagged)
print("Sentence:", sentence)
print("POS Tags:", tagged)
print("Chunk Tree:", tree)
print("\nError Analysis:")
print("The grammar may miss complete verb phrases.")
print("It may also fail to include adverbs or auxiliary verbs")
print("inside a single VP chunk.")
print("Improvement: Extend the VP rule to include auxiliaries,")
print("adverbs, and main verbs.")