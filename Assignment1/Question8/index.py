#-------------------------------------------------------------------------
# AUTHOR: Nathan Li
# FILENAME: index.py
# SPECIFICATION: Builds an inverted index from a document collection using lemmatization and surface-level normalization
# FOR: CS 4250 - Assignment #1
# TIME SPENT: 
#-------------------------------------------------------------------------

# Importing Python libraries
import pandas as pd

# Reading the document collection
data = pd.read_csv("collection.csv")



# Defining the dictionary used for lemmatization
# --> add your Python code here
lemmas = {
    "homes": "home",
    "increases": "increase",
    "rising": "rise",
    "increasing": "increase",
    "sales": "sale",
}

# Creating the data structure that will store the inverted index
invertedIndex = {}

# Processing each document in the collection
for i, row in data.iterrows():

    docID = row["Document"]
    text = row["Text"]

    # Applying surface-level normalization
    # --> add your Python code here
    text = text.lower().strip()
    text = text.translate(str.maketrans("", "", ".,!?;:()[]{}\"'"))  # Remove punctuation

    # Tokenizing the document
    # --> add your Python code here
    tokens = text.split()


    # Applying lemmatization
    # --> add your Python code here
    tokens = [lemmas.get(token, token) for token in tokens]


    # Building the inverted index
    # --> add your Python code here
    for token in tokens:
        if token not in invertedIndex:
            invertedIndex[token] = []
        invertedIndex[token].append(docID)
        if docID not in invertedIndex[token]:
            invertedIndex[token].append(docID)

# Printing the inverted index with terms ordered alphabetically
# Expected format:
# term1 : ['Doc1', 'Doc2']
# term2 : ['Doc3']
# --> add your Python code here

for token in sorted(invertedIndex):
    print(token, ":", invertedIndex[token])