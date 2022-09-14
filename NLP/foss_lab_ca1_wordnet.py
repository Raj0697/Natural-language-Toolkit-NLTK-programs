from nltk.corpus import wordnet 
syns = wordnet.synsets("Friends")
print("Definition of the said word:")
print(syns[0].definition())
print("\nExamples of the word in use::")
print(syns[0].examples())