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
stop = set(stopwords.words("english"))
stopwords=set()
for words in stop:
	shit=words.encode('UTF-8')
	stopwords.add(shit)
stop=stopwords

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
i=0
direc = os.getcwd()
keydirec = os.getcwd()
keydirec = keydirec + '/keydirec/'
direc = direc + '/temp2/'
for filename in os.listdir(direc):
	i+=1	
data=[[] for j in range(i)]
key = [[] for j in range(i)]
dt=[[] for j in range(i)]
reload(sys)  
sys.setdefaultencoding('utf8')
i=0
k = 0
for filename in os.listdir(direc):
	print filename
	keyname = filename.split(".")
	keyname[0] = keyname[0] + ".key"
	temp = direc + filename
	tempkey = keydirec + keyname[0] 
	f= open(temp,"r")
	keyf = open(tempkey,"r")
 	temp=set()
	terms_only=[]
	for line in f:
		for term in preprocess(line):
#			term = ps.stem(term)
			term=term.encode('UTF-8')
			if term.lower() not in stop:
				terms_only.append(term.lower())
		for char in terms_only:
#			char=ps.stem(char)
			temp.add(char)
			data[i].append(char)
		terms_only = []
	i+=1
	temp = []
	for line in keyf:
		for keyword in preprocess(line):
			temp.append(keyword)
	key[k].append(temp)
# 	print key[k]	  
	k = k+1	

i=0
while i < len(data):
	j=0
	all_words = nltk.FreqDist(data[i])
	while j < len(data[i]):
		if all_words[data[i][j]] >= 1:
			dt[i].append(data[i][j])
		j+=1
	i+=1
