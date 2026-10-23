import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
text = "The cats are running faster than the dogs. They played happily."
words = word_tokenize(text)
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
print("Original Words:")
print(words)
print("\nStemmed Words:")
print(stemmed_words)