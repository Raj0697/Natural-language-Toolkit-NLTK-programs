from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from matplotlib import pyplot as plt

text = """Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""

# sentence tokenization
tokenized_text = sent_tokenize(text)
print("Sentence tokenization : " , tokenized_text)

# word tokenization
tokenized_word = word_tokenize(text)
print("\n\nWord tokenization : ", tokenized_word)

# Frequency distribution
fdist = FreqDist(tokenized_word)
print("\n\nFrequency distribution : ", fdist)
print("\n\nMost common Frequency distribution :" ,fdist.most_common(2))

fdist.plot(30,cumulative=False)
plt.show()