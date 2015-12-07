import sys
import re
import string
from string import punctuation
from operator import itemgetter
import operator
from sklearn.cluster import KMeans
import numpy as np
from json import dumps
from nltk.corpus import stopwords

def vectorize(reviewdict, freq500):
	vectors = []
	for review in reviewdict:
		templist = []
		for word in freq500:
			if word in review['wordcounts']:
				templist.append(review['wordcounts'][word])
			else:
				templist.append(0)
		vectors.append({'id': review['id'], 'rating': review['rating'], 'wordvector': templist})
	return vectors

path = "./smallfoods.txt"        
fullText = ""
outputfile = 'out.json'
sys.stdout = open(outputfile, 'w')
#The code for parsing was adapted from Humphrey Mensa

allowedNonAlphanum = [" ", ":", ",", "-", "(", ")", "!", "\n", "\r","."]

with open(path) as f:
	while True:
		c = f.read(1)
                if not c:
                        break
                if c.isalnum() or c in allowedNonAlphanum:
                        if "\r" in c:
                                fullText = fullText + "\n"
                        elif "." in c:
                                fullText = fullText + " "
                        elif "(" in c:
                                fullText = fullText + ""
                        elif ")" in c:
                                fullText = fullText + ""
                        elif "-" in c:
                                fullText = fullText + ""            
                        elif "!" in c:
                                fullText = fullText + ""            
                        elif "," in c:
                                fullText = fullText + ""            
                        else:
                                fullText = fullText + c
fullText = fullText.replace("\n","yy")
review_list = []
reviewscore = re.findall(r'(?<=reviewscore:).*?(?=yy)',fullText)
review = re.findall(r'(?<=reviewtext:).*?(?=yyyy)',fullText)
reviewscore = [int(item[1]) for item in reviewscore]
review = [item.lower() for item in review]
review_pun_removed = review
cachedStopWords = stopwords.words("english")
for x in review:
    words = x.split()
    newwords = []
    for word in words:
	    if word not in cachedStopWords:
		    newwords.append(word)
    review_list.append(newwords)
#End of Humphrey's code.

reviewsdict = []
count = 1
for i in range(len(review_list)):
	tempdict = {}
	review = review_list[i]
	for word in review:
		if word not in tempdict:
			tempdict[word] = 1
		else:	
			tempdict[word] = tempdict[word] + 1
	reviewsdict.append({'id': count, 'rating': reviewscore[i], 'wordcounts': tempdict})
	count += 1

finaldict = {}
for each in reviewsdict:
	for key in each['wordcounts']:
		if key in finaldict:
			finaldict[key] = finaldict[key] + each['wordcounts'][key]
		else:
			finaldict[key] = each['wordcounts'][key]

sortedfinaldict = sorted(finaldict.items(), key = lambda item: item[1], reverse=True)    
freq500words = []
freq500wordcounts = []

for i in range(100):
	freq500words.append(sortedfinaldict[i][0])
	freq500wordcounts.append(sortedfinaldict[i][1])

review_vectors = vectorize(reviewsdict, freq500words)
unclustered_data = [None] * len(review_vectors)
for row in review_vectors:
	ix = row['id'] - 1
	unclustered_data[ix] = [float(elm) for elm in row['wordvector']]

kmeans = KMeans(n_clusters=10, init='k-means++', random_state = 32)
kmeans.fit(unclustered_data)
prototypes = kmeans.cluster_centers_
clustered = kmeans.predict(unclustered_data)

jsonob = []
for row in review_vectors:
	baseob = {}
	for key in row:
		if key == 'wordvector':
			for i in range(len(row[key])):
				baseob['wc_' + freq500words[i]] = row[key][i]
		elif key != 'id':
			baseob[key] = row[key]
		else:
			baseob[key] = row[key]

	baseob['cluster'] = int(clustered[row['id'] - 1])
	jsonob.append(baseob)

print dumps(jsonob)
