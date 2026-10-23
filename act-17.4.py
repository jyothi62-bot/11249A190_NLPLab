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
print("\nACTIVITY 4: Campus Sentence Mini-Project")
sentences = [
    "The professor teaches in the classroom.",
    "Students read books in the library.",
    "The young researcher develops an application.",
    "The students are studying in the laboratory.",
    "Our university has a large campus."]
for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    tree = chunker.parse(tagged)
    print("\nSentence:", sentence)
    print("Chunk Tree:", tree)

