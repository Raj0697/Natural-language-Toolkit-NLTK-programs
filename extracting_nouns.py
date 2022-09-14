import spacy

text="James works at Microsoft. She lives in manchester and likes to play the flute"

# Coverting the text into a spacy Doc
nlp=spacy.load("D:/en_core_web_sm")
doc=nlp(text)

# Using spacy's pos_ attribute to check for part of speech tags
for token in doc:
  if token.pos_=='NOUN' or token.pos_=='PROPN':
    print(token.text)
