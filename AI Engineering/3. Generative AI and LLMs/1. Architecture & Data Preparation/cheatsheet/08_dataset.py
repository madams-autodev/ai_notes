"""
The Dataset class enables accessing and retrieving individual samples from a data set.
The code example shows how you can create a custom data set and access samples.
"""


# Imports the Dataset class and defines a list of sentences
from torch.utils.data import Dataset
sentences = ["If you want to know what a man's like, take a 
good look at how he treats his inferiors, not his equals.", 
"Fae's a fickle friend, Harry."]
# Downloads and reads data
class CustomDataset(Dataset):
    def __init__(self, sentences):
        self.sentences = sentences
    # Returns the data length
    def __len__(self):
        return len(self.sentences)
    # Returns one item on the index
    def __getitem__(self, idx):
        return self.sentences[idx]
# Creates a dataset object
dataset=CustomDataset(sentences)
# Accesses samples like in a list
E.g., dataset[0]