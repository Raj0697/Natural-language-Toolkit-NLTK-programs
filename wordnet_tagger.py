from taggers import WordNetTagger 
from nltk.corpus import treebank 
  
# Initializing 
default_tag = DefaultTagger('NN') 
  
# initializing training and testing set     
train_data = treebank.tagged_sents()[:3000] 
test_data = treebank.tagged_sents()[3000:] 
  
wn_tagging = WordNetTagger() 
a = wn_tagger.evaluate(test_data) 
  
print ("Accuracy of WordNetTagger : ", a) 
