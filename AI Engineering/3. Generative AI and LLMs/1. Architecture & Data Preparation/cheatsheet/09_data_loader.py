"""
A DataLoader class enables efficient loading and iteration over data sets for training deep learning models.
The code example shows how you can use the DataLoader class to generate batches of sentences for further processing, such as training a neural network model
"""

# Creates an iterator object
data_iter = iter(dataloader)
# Calls the next function to return new batches of samples
next(data_iter)
# Creates an instance of the custom data set
from torch.utils.data import DataLoader

custom_dataset = CustomDataset(sentences)
# Specifies a batch size
batch_size = 2
# Creates a data loader
dataloader = DataLoader(custom_dataset, batch_size=batch_size, shuffle=True)
# Prints the sentences in each batch
for batch in dataloader:
    print(batch)
