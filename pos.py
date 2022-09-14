# Loading Libraries 
from nltk.tag import DefaultTagger 
import nltk

# Defining Tag 
tagging = DefaultTagger('NN') 

print(tagging.tag_sents([['welcome', 'to', '.'], ['mcc', 'in', 'chennai']]) )

sent = "Albert Einstein was born in Ulm, Germany in 1879."
tokens=nltk.word_tokenize(sent)
print(tokens)