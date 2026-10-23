import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
text = "I love Natural Language Processing."
tokens = word_tokenize(text)
print(tokens)