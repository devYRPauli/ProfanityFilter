import sys
import time






try:
    from nltk import wordpunct_tokenize
    from nltk.corpus import stopwords
    print("nltk is installed. \n")
except ImportError:
    print("You need to install nltk (http://nltk.org/index.html)")






def calculate_languages_ratios(text):
    languages_ratios = {}
    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]

    # Compute per language included in nltk number of unique stopwords appearing in analyzed text
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)

        languages_ratios[language] = len(common_elements)  # language "score"

    return languages_ratios






def load_bad_words(language):
    if language.upper() in ['ENGLISH','FRENCH','SPANISH','GERMAN']:
        badwords_list = []
        lang_file = open('datasets/'+language.lower()+'.csv','r')
        for word in lang_file:
            badwords_list.append(word.lower().strip('\n'))
    return badwords_list






def detect_language(text):
    ratios = calculate_languages_ratios(text)
    most_rated_language = max(ratios, key=ratios.get)
    return most_rated_language






print ("Language can be in the form of: english, french, german and spanish.")
print ('\n')
testlang = input ("Language to test: ")
print('\n')
filename = 'test-files/'+testlang.lower()+'.txt'
file = open(filename,'r')
text = ''
line_count = 1
for i in file:
	text += str(line_count)+'| '+i
	line_count+=1
time.sleep(2)






print ('----------------------Input Text----------------------')
print ('\n')
print (text)
print ('\n')
print ('-----------------------Text Read-----------------------')
print ('\n')
language = detect_language(text)
print ('\n')
time.sleep(1)
print ('----------------------------')
print ('Language Detected: ',language.upper())
print ('----------------------------')
print ('\n')
time.sleep(1)
print ('----------------------------------------')
print ('Checking for offensive words in '+language.upper()+'.')
print ('----------------------------------------')
print ('\n')
badwords = load_bad_words(language)
badwords = set(badwords)
text_list = text.split('\n')






for sentence in text_list:
	line_number = str(text_list.index(sentence)+1)
	for key in ['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']:
		sentence = sentence.replace(key,'')
	abuses = [i for i in sentence.lower().split() if i in badwords]
	if abuses == []:
		continue
	else:
		time.sleep(0.5)
		print (str(len(abuses))+' Offensive Words found at line number: '+line_number)
		x_words=''
		for i in abuses:
			x_words+=i+', '
		print ('Offensive Words: '+x_words[:-2])
		print ('\n')
