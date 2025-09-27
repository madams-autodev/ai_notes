"""
The vocab object is part of the PyTorch torchtext library. It maps tokens to indices.
The code example shows how you can apply the vocab object to tokens directly.
"""


# Takes an iterator as input and extracts the next tokenized sentence.
# Creates a list of token indices using the vocab dictionary for each token.
def get_tokenized_sentence_and_indices(iterator):
    tokenized_sentence = next(iterator)
    token_indices = [vocab[token] for token in tokenized_sentence]
    return tokenized_sentence, token_indices


# Returns the tokenized sentences and the corresponding token indices.
# Repeats the process.
tokenized_sentence, token_indices = get_tokenized_sentence_and_indices(my_iterator)
next(my_iterator)
# Prints the tokenized sentence and its corresponding token indices.
print("Tokenized Sentence:", tokenized_sentence)
print("Token Indices:", token_indices)
