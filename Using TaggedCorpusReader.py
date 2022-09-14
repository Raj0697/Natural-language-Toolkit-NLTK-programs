# Using TaggedCorpusReader 
from nltk.corpus.reader import TaggedCorpusReader 

# intitializing 
x = TaggedCorpusReader('.', r'.*\.pos') 

words = x.words() 
print ("Words : \n", words) 

tag_words = x.tagged_words() 
print ("\ntag_words : \n", tag_words) 
