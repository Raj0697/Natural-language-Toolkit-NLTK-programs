from nltk.tokenize import sent_tokenize

text = """Dropbox is a personal cloud storage service (sometimes referred to as an online backup service) 
that is frequently used for file sharing and collaboration. The Dropbox application is available for Windows,
 Macintosh and Linux desktop operating systems. There are also apps for iPhone, iPad, Android, and BlackBerry devices.
"""

text2="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""
tokenized_text=sent_tokenize(text)
tokenized_text2=sent_tokenize(text2)
print("sentence tokenization :", tokenized_text)
print("\nsentence tokenization :", tokenized_text2)

from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(text)
print("\ntokenized_word :", tokenized_word)