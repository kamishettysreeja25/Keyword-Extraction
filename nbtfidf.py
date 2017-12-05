import math
import prunecp
import nltk
x = prunecp.dt
testing = prunecp.data
no_of_documents = len(x)
#phrase t,document d,t appears in n of N documents in D
def count(phrase):
	total = 0
	for i in range(0,no_of_documents):
		for j in range(0,len(x[i])):
			if x[i][j] == phrase:
				total = total+1
	return total		
def tf(t,d):
	freq = 0
	for j in range(0,len(d)):
		if t == d[j]:
			freq = freq + 1
	return float(freq)
def idf(n,m):
	if n!=0  and (m/n)>0:
		return float(math.log(m/n,10))
	else:
		return 0
def tfidf(t,d,n,m):
	
	return float(tf(t,d) * idf(n,m))
def distance(phrase,document):
	for i in range(0,len(document)):
		if document[i] == phrase:
			return float(i+1)
def frequency(phrase,document):
	freq = 0 
	for i in range(0,len(document)):
		if document[i] == phrase:
			freq = freq + 1
	return float(freq/float(len(document)))
problist = []
keywords = [[] for j in range(no_of_documents)]
keywordfinal = [[] for j in range(no_of_documents)]
def main():
	for i in range(0,no_of_documents):
		tempkeylist = []
		for j in range(0,len(x[i])):
			total_freq = count(x[i][j])
			tvalue = float(tfidf(x[i][j],x[i],total_freq,no_of_documents))
			dist = distance(x[i][j],x[i])  #distance of the word from the beginning
			pr = frequency(x[i][j],x[i]) #probability of that word to be a key
			prdkey = 1 - dist/len(x[i]) #probability that word occurs at that distance D
			evidence = 1.00 #change according to the probability values
			prob = (tvalue * prdkey)/evidence
			temp = [tvalue,x[i][j]]
			problist.append(temp)
			tempkeylist.append(temp)
		keywords[i] = tempkeylist
		f = 0
		temp = set()
		while f < len(keywords[i]):
			if keywords[i][f][1] not in temp:
				temp.add(keywords[i][f][1])
				keywordfinal[i].append(keywords[i][f][1])
			f = f+1
		topkey = list(keywordfinal[i])[:15]	
		print topkey
		print prunecp.key[i]
#		classifier = nltk.NaiveBayesClassifier.train(testing[:1900])
#		print classifier
		#print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)

	temp=set()
	k=0
	final=[]
	while k < len(problist):
		if problist[k][1] not in temp:
			temp.add(problist[k][1])
			final.append(problist[k])
		k+=1
	topk = list(final)[:200]	
#print topk  
main()
