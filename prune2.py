import sys
import re
import json
import operator 
from nltk.corpus import stopwords
import string
from collections import Counter
from collections import defaultdict
from collections import OrderedDict
import vincent
import pandas
from nltk.stem import WordNetLemmatizer
import os
import sys
import nltk  
from nltk.stem import PorterStemmer

ps = PorterStemmer()

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']
#stop = set(stopwords.words("english"))
stop.append('u\'the\'')
print stop
#wordnet_lemmatizer = WordNetLemmatizer()
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,

    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r'[a-zA-Z\d\s:]'

    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
 #   r'(?:(?:\w)+(?:\d)+?)', # numbers
 #   r'(?:(?:\w+\d+,?)+(?:\.?\w+\d+)?)', # numbers
 #   r'(?:(?:\d)+(?:\w)+?)', # numbers
 # r'(?:[0-9])*'
 # r"(?:[^0-9]+)"
#  r"(?:%[0-9a-z])*'
    #r'(?:[\w+])', # other words
    #r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

'''fname = 'project.json'
with open(fname, 'r') as f:
    
    r=open("out.txt",'w')
    count_all = Counter()


    for line in f:
        temp=set()
	strs=line
	match = re.search(r'\btext\b',strs)
	if match:
		print line
        	terms_only = [term.lower() for term in preprocess(line) if term not in stop]
                count_all.update(terms_only)
		for char in terms_only:
			if char not in temp and count_all[char] > 5:
				char= wordnet_lemmatizer.lemmatize(char)
				temp.add(char)
				r.write(char)
				r.write(" ")
		print terms_only
		r.write("\n")'''

i=0
direc = os.getcwd()
direc = direc + '/temp/'
for filename in os.listdir(direc):
	i+=1	
data=[[] for j in range(i)]
reload(sys)  
sys.setdefaultencoding('utf8')
i=0
for filename in os.listdir(direc):
	print filename
	temp = direc + filename 
        f= open(temp,"r")
 	temp=set()
	terms_only=[]
	#print stop
	for line in f:
		for term in preprocess(line):
			term = ps.stem(term)
			if term not in stop:
	#			print term
				terms_only.append(term.lower())
		#terms_only = [term.lower() for term in preprocess(line) if term not in stop]
		#print terms_only
		for char in terms_only:
	#		if char not in temp:
			char=ps.stem(char)
	#		print char
			temp.add(char)
			data[i].append(char)
		terms_only = []
	i+=1
print data[0][0]

i=0
direc = os.getcwd()
direc = direc + '/temp/'
for filename in os.listdir(direc):
        i+=1

dt=[[] for j in range(i)]
i=0
while i < len(data):
	j=0
	all_words = nltk.FreqDist(data[i])
	while j < len(data[i]):
		if all_words[data[i][j]] > 50:
			dt[i].append(data[i][j])
		j+=1
	i+=1

print dt[0][0]

