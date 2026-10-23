import nltk
from nltk import word_tokenize
from nltk.tag import RegexpTagger
nltk.download('punkt')
nltk.download('punkt_tab')
patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*ly$', 'RB'),
    (r'.*ous$', 'JJ'),
    (r'.*ness$', 'NN'),
    (r'.*able$', 'JJ'),
    (r'.*', 'NN')
]
tagger = RegexpTagger(patterns)
paragraph = (
    "The scientists carefully examined the newly discovered species. "
    "They quickly noted its unusual behaviour and recorded their findings "
    "in a detailed report."
)
tokens = word_tokenize(paragraph)
tagged = tagger.tag(tokens)
print(tagged)
