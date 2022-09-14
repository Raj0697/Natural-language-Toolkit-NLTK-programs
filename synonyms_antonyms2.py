from nltk.corpus import wordnet   #Import wordnet from the NLTK
synset = wordnet.synsets("relationship")
print('\n\nWord and Type : ' + synset[0].name())
print('\nSynonym of word is: ' + synset[0].lemmas()[0].name())
print('\nThe meaning of the word : ' + synset[0].definition())
print('\nExample of word : ' + str(synset[0].examples()))