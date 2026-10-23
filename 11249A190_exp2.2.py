import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')
text = "Hello! Welcome to NLP. Tokenization is important."
sentences = sent_tokenize(text)
words = word_tokenize(text)
print("Sentences:")
print(sentences)
print("\nWords:")
print(words)