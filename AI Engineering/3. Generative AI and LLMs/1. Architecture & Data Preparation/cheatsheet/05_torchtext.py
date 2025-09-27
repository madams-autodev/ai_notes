"""
The torchtext library is part of the PyTorch ecosystem and provides the tools and functionalities required for NLP.
The code example shows how you can use torchtext to generate tokens and convert them to indices.
"""

from torchtext.vocab import build_vocab_from_iterator

# Defines a dataset
dataset = [
    (1, "Introduction to NLP"),
    (2, "Basics of PyTorch"),
    (1, "NLP Techniques for Text Classification"),
    (3, "Named Entity Recognition with PyTorch"),
    (3, "Sentiment Analysis using PyTorch"),
    (3, "Machine Translation with PyTorch"),
    (1, "NLP Named Entity,Sentiment Analysis, Machine Translation"),
    (1, "Machine Translation with NLP"),
    (1, "Named Entity vs Sentiment Analysis NLP"),
]
# Applies the tokenizer to the text to get the tokens as a list
from torchtext.data.utils import get_tokenizer

tokenizer = get_tokenizer("basic_english")
tokenizer(dataset[0][1])


# Takes a data iterator as input, processes text from the iterator,
# and yields the tokenized output individually
def yield_tokens(data_iter):
    for _, text in data_iter:
        yield tokenizer(text)


# Creates an iterator
my_iterator = yield_tokens(dataset)
# Fetches the next set of tokens from the data set
next(my_iterator)
# Converts tokens to indices and sets <unk> as the
# default word if a word is not found in the vocabulary
vocab = build_vocab_from_iterator(yield_tokens(dataset), specials=["<unk>"])
vocab.set_default_index(vocab["<unk>"])
# Gives a dictionary that maps words to their corresponding numerical indices
vocab.get_stoi()
