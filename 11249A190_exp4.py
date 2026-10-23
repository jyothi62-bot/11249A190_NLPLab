import nltk
from nltk.stem import WordNetLemmatizer
nltk.download("wordnet")
lemmatizer = WordNetLemmatizer()
words = ["running", "better", "cars", "children"]
pos = ["v", "a", "n", "n"]
print("Word\tLemma")
for word, p in zip(words, pos):
    print(word, "\t\t", lemmatizer.lemmatize(word, p))