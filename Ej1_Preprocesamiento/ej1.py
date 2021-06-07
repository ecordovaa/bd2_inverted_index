import nltk
from nltk.stem.snowball import SnowballStemmer

def defineStopwords():
	with open('Ej1_Preprocesamiento/stoplist.txt') as stoplist:
		return nltk.word_tokenize(stoplist.read().lower())

def removeUnnecesarySymbols(word):
	unnecesarySymbols = {"<", ">", ",", "º", ":", ";", "«", "»", ".", "!", "¿", "?", ")", "("}
	filter = ""
	for statement in word:
		if(statement in unnecesarySymbols):
			statement = statement.replace(statement, "")
		filter += statement
	return filter

def readBook(bookNumber):
	stopwords = defineStopwords()
	stemmer = SnowballStemmer(language='spanish')
	with open("Ej1_Preprocesamiento/books/"+str(bookNumber)+".txt") as book, open("Ej1_Preprocesamiento/preprocesados/"+str(bookNumber)+".txt", 'w') as result:
		for term in book.read().split():
			term = term.lower()
			term = removeUnnecesarySymbols(term)
			if term not in stopwords:
				term = stemmer.stem(term)
				result.write(term + "\n")