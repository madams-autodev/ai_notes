import nltk

nltk.download("punkt")
from nltk.tokenize import word_tokenize

text = "Unicorns are real. I saw a unicorn yesterday. I couldn't see it today."
token = word_tokenize(text)
print(token)

"""
NLTK is a Python library used in natural language processing (NLP) for tasks such as tokenization and text processing. 
The code example shows how you can tokenize text using the NLTK word-based tokenizer.
"""
