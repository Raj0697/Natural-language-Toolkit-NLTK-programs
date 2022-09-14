import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
   
# Input text - to summarize 
try:
    text = """Mark Elliot Zuckerberg (born May 14, 1984) is an American media magnate, internet entrepreneur, and philanthropist. He is known for co-founding Facebook, Inc. and serves as its chairman, chief executive officer, and controlling shareholder. He also is a co-founder of the solar sail spacecraft development project Breakthrough Starshot and serves as one of its board members.[5]
Born in White Plains, New York, Zuckerberg attended Harvard University, where he launched the Facebook social networking service from his dormitory room on February 4, 2004, with college roommates Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, and Chris Hughes.[6] Originally launched to select college campuses, the site expanded rapidly and eventually beyond colleges, reaching one billion users by 2012. Zuckerberg took the company public in May 2012 with majority shares. In 2007, at age 23, he became the world's youngest self-made billionaire. As of September 2020, Zuckerberg's net worth is $111 billion,[7] making him the 4th-richest person in the world.[8] He is the only person under 40-years-old in Forbes' list of the 20 richest people.[9]
Since 2010, Time magazine has named Zuckerberg among the 100 wealthiest and most influential people in the world as a part of its Person of the Year award. In December 2016, Zuckerberg was ranked 10th on Forbes list of The World's Most Powerful People."""
   
    # Tokenizing the text
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)
       
    # Creating a frequency table to keep the 
    # score of each word
       
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
       
    # Creating a dictionary to keep the score
    # of each sentence
    sentences = sent_tokenize(text)
    sentenceValue = dict()
       
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq
       
       
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]
       
    # Average value of a sentence from the original text


    average = int(sumValues / len(sentenceValue))


    # Storing sentences into our summary.
    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.4 * average)):
            summary += " " + sentence
    print(summary)
    print("Average words : ",average)
    print("frequency : ",freq)
except Exception as e:
    raise e

