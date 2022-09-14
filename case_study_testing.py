import PyPDF2
import nltk
#nltk.download()

pdffile = open('D:/RajKumar report.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(pdffile)
print('Number of pages found in the pdf : ',pdfreader.numPages)
pageobj = pdfreader.getPage(0)
print('The text extracted from the pdf :\n\n\t',pageobj.extractText())
pdffile.close()