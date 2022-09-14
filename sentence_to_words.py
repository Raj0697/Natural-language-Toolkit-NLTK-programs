import nltk
from nltk.tokenize import sent_tokenize,word_tokenize

text = '''
Joe waited for the train. The train was late. 
Mary and Samantha took the bus. 
I looked for Mary and Samantha at the bus station.
'''
print("\nOriginal string:")
print(text)

token_text = word_tokenize(text)
sentence_text = sent_tokenize(text)

print("Word-tokenized copy in a list:\n")
print(token_text)
print("\nRead the list:")
for s in token_text:
    print(s)

print(sentence_text)
print("\nRead the list:")
for n in sentence_text:
	print(n)