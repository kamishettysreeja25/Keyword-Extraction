import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# randomising data for testing and training set
random.shuffle(documents)
stop_words = set(stopwords.words("english"))

# filtering the words
filtered_sentence = []

for w in words:
  if w not in stop_words:
    filtered_sentence.append(w)

all_words = []

for w in filtered_sentence.words():
    all_words.append(w.lower())

# calculating the frequency of words
all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

featuresets = [(find_features(rev), category for (rev,category) in documents]
# set that we'll train our classifier with
training_set = featuresets[:1900]

# set that we'll test against.
testing_set = featuresets[1900:]
