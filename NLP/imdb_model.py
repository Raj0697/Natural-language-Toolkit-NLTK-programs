import nltk
import pandas as pd
from matplotlib import pyplot as plt

traindata = pd.read_csv("E:/IMDB-Movie-Data.csv")
traindata
# display available data
traindata.head()

print(traindata.columns)
traindata['Description'][0]

print(traindata.dtypes)

traindata.describe()

traindata.info()

traindata.isna()

# getting the count of null values in particular columns
traindata.isna().sum()

traindata['Description'][0]

traindata['sentence_clean'] = traindata['sentence'].str.replace('[{}]'.format(string.punctuation), '')
traindata['sentence_clean'] = traindata['sentence_clean'].str.lower()
traindata['sentence_clean'] = '<s ' + traindata['sentence_clean']
traindata['sentence_clean'] = traindata['sentence_clean'] + ' /s>'
traindata.head()

text = traindata['sentence_clean']
text_list = " ".join(map(str, text))
text_list[0:100]
