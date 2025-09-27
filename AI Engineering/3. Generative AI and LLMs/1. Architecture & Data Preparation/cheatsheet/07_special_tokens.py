"""
Special tokens are tokens introduced to input sequences to convey specific information or serve a particular purpose during training.
The code example shows the use of <bos> and <eos> during tokenization. The <bos> token denotes the beginning of the input sequence, and the <eos> token denotes the end.
"""

# Appends <bos> at the beginning and <eos> at the end of the tokenized sentences
# using a loop that iterates over the sentences in the input data
tokenizer_en = get_tokenizer("spacy", language="en_core_web_sm")
tokens = []
max_length = 0
for line in lines:
    tokenized_line = tokenizer_en(line)
    tokenized_line = ["<bos>"] + tokenized_line + ["<eos>"]
    tokens.append(tokenized_line)
    max_length = max(max_length, len(tokenized_line))


# The code example shows the use of <pad> token to ensure all sentences have the same length.
# Pads the tokenized lines
for i in range(len(tokens)):
    tokens[i] = tokens[i] + ["<pad>"] * (max_length - len(tokens[i]))
