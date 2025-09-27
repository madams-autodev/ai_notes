"""
The custom collate function is a user-defined function that defines how individual samples are collated or batched together. You can utilize the collate function for tasks such as tokenization, converting tokenized indices, and transforming the result into a tensor.
The code example shows how you can use a custom collate function in a data loader.
"""


# Defines a custom collate function
def collate_fn(batch):
    tensor_batch = []
    # Tokenizes each sample in the batch
    for sample in batch:
        tokens = tokenizer(sample)
        # Maps tokens to numbers using the vocab
        tensor_batch.append(torch.tensor([vocab[token] for token in tokens]))
    # Pads the sequences within the batch to have equal lengths
    padded_batch = pad_sequence(tensor_batch, batch_first=True)
    return padded_batch


# Creates a data loader using the collate function and the custom dataset
dataloader = DataLoader(
    custom_dataset, batch_size=batch_size, shuffle=True, collate_fn=collate_fn
)
