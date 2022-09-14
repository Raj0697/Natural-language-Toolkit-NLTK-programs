from numpy import arange
from matplotlib import pyplot
import nltk

colors = 'rgbcmyk'  # red, green, blue, cyan, magenta, yellow, black

def bar_chart(categories, words, counts):
	ind = arange(len(words))
	width = 1 / (len(categories) + 1)
	bar_groups = []
	for c in range(len(categories)):
		bars = pyplot.bar(ind+c*width, counts[categories[c]], width,color=colors[c % len(colors)])
		bar_groups.append(bars)

	pyplot.xticks(ind+width, words)
	pyplot.legend([b[0] for b in bar_groups], categories, loc='upper left')
	pyplot.ylabel('Frequency')
	pyplot.title('Frequency of six modal verbs by genre')
	pyplot.show()

genres = ['news','religion','hobbies','government','adventure']
modals = ['can','could','may','might','must','will']
cfdist = nltk.ConditionalFreqDist((genre,word)
for genre in genres
for word in nltk.corpus.brown.words(categories=genre)
if word in modals)

counts = {}
for genre in genres:
	counts[genre] = [cfdist[genre][word]for word in modals]
	bar_chart(genres,modals,counts)