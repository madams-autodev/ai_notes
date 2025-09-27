"""
XLNetTokenizer tokenizes text using Unigram and SentencePiece algorithms.
The code example shows how you can tokenize text using XLNetTokenizer.
"""

from transformers import XLNetTokenizer

tokenizer = XLNetTokenizer.from_pretrained("xlnet-base-cased")
tokenizer.tokenize("IBM taught me tokenization.")
