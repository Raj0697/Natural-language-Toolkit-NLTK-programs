
text="He is a gret person. He beleives in bod"
import textblob
from textblob import TextBlob

# Using textblob's correct() function
text=TextBlob(text)
print(text.correct())