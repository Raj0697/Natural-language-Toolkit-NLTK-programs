import nltk
from nltk.corpus import stopwords

stop_words=set(stopwords.words("english"))
print("common stop words in english: \n\n", stop_words)