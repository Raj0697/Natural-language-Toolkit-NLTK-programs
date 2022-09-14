import nltk
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from matplotlib import pyplot as pyplot
from nltk import DefaultTagger

wordnet_lemmatizer = WordNetLemmatizer()

sentence = "He was running and eating at same time. He has bad habit of swimming after playing long hours in the Sun."
punctuations="?:!.,;"
sentence_words = nltk.word_tokenize(sentence)
for word in sentence_words:
    if word in punctuations:
        sentence_words.remove(word)

sentence_words
print("{0:20}{1:20}".format("Word","Lemma"))
for word in sentence_words:
    print ("\n\n{0:20}{1:20}".format(word,wordnet_lemmatizer.lemmatize(word)))


#------------------------------------------------------------------------------------
# POS tagging

text = word_tokenize("They refuse to permit us to obtain the refuse permit")
nltk.pos_tag(text)
print(text)
sent = "Albert Einstein was born in Ulm, Germany in 1879."

tokens=nltk.word_tokenize(sent)
print(tokens)

['Albert', 'Einstein', 'was', 'born', 'in', 'Ulm', ',', 'Germany', 'in', '1879', '.']

nltk.pos_tag(tokens)


from nltk.corpus import wordnet 
syns = wordnet.synsets("fight")
print("\n\n\nDefinition of the given word:")
print(syns[0].definition())
print("\nExamples of the word in use::")
print(syns[0].examples())