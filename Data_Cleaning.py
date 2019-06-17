import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np


def remove_non_ascii(text):
    i =int()
    return ''.join(i for i in text if ord(i)<128)


# Load the Data
changedFile = pd.read_csv('C://Users//Vanya//PycharmProjects//Fakenews//Replacedfile.csv', dtype={'News':str,'Label':str},na_values=" ")

changedFile['News']= changedFile['News'].dropna().apply(remove_non_ascii)
print(changedFile.tail())
train, test = train_test_split(changedFile, test_size=0.2)
print(train.shape)
print(test.shape)
print(changedFile, 10)

# Change the data type
# train['Label'] = train['Label'].astype('bool')
# test['Label'] = test['Label'].astype('bool')

# Clean the data

train.dropna(how='all',axis='columns')  # Removing rows with all NA values
print(train.shape)
train['Label'].dropna()  # Removing data if label is empty
train['News'].isnull()
train['News'].dropna()   # Removing data if news is empty
train.drop_duplicates(keep='first', inplace=False) # Removing duplicates

test.dropna(how='all')   # Removing rows with all NA values
test['Label'].dropna()  # Removing column if label is empty
test['News'].dropna()  # Removing data if news is empty
test.drop_duplicates(keep='first', inplace=False)  # Removing duplicates.
print(train,10)
print("Cleaned Training and testing data ")
print(train.shape)
print(test.shape)


train.to_csv("train.csv")
test.to_csv("test.csv")