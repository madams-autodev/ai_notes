from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
tokenizer.tokenize("IBM taught me tokenization.")

"""
	BertTokenizer is a subword-based tokenizer that uses the WordPiece algorithm. 
    The code example shows how you can tokenize text using BertTokenizer.
"""
