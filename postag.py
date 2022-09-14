import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
stop_words = set(stopwords.words('english')) 

#Dummy text 
txt = """Python is an interpreted, object-oriented, high-level programming
 language with dynamic semantics. Its high-level built in data structures,
  combined with dynamic typing and dynamic binding, make it very attractive
   for Rapid Application Development, as well as for use as a scripting or 
   glue language to connect existing components together.
"""

# sent_tokenize is one of instances of 
# PunktSentenceTokenizer from the nltk.tokenize.punkt module 

tokenized = sent_tokenize(txt) 
for i in tokenized: 
	
	# Word tokenizers is used to find the words 
	# and punctuation in a string 
	wordsList = nltk.word_tokenize(i) 

	# removing stop words from wordList 
	wordsList = [w for w in wordsList if not w in stop_words] 

	# Using a Tagger. Which is part-of-speech 
	# tagger or POS-tagger. 
	tagged = nltk.pos_tag(wordsList) 

	print(tagged) 
