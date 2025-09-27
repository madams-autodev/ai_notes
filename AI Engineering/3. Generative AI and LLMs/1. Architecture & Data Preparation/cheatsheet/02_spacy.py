import spacy

text = "Unicorns are real. I saw a unicorn yesterday. I couldn't see it today."
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
token_list = [token.text for token in doc]
print("Tokens:", token_list)


"""
spaCy is an open-source library used in NLP. It provides tools for tasks such as tokenization and word embeddings. 
The code example shows how you can tokenize text using spaCy word-based tokenizer.
"""
