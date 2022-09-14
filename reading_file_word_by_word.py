import nltk

print('These are the following words found in the text file : \n\n')
f = open('D:/IOT.txt','r')
count = 0

content = f.read()
lines = content.split('\n')

for i in lines:
	if i:
		count+=1


with open('D:/IOT.txt','r') as file:
	for line in file:
		for word in line.split():
			print('\t', word)
		

print('\n\nThis is the original file : \n\n\t', content)
print('\n\n This is the number of lines in the file : ', count)