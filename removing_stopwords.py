import nltk
from nltk.corpus import stopwords

text = '''the outbreak of coronavirus disease 2019 (COVID-19) has created a global health.'''
my_stopwords=set(stopwords.words('english'))
new_tokens=[]

# Tokenization using word_tokenize()
all_tokens=nltk.word_tokenize(text)

for token in all_tokens:
  if token not in my_stopwords:
    new_tokens.append(token)

" ".join(new_tokens)
print(new_tokens)