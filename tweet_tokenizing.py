import re

text=" Having lots of fun #goa #vaction #summervacation. Fancy dinner @Beachbay restro :) "
# Cleaning the tweets
text=re.sub(r'[^\w]', ' ', text)

# Using nltk's TweetTokenizer
from nltk.tokenize import TweetTokenizer
tokenizer=TweetTokenizer()
print(tokenizer.tokenize(text))