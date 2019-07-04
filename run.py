# -*- coding: utf-8 -*-
"""
Created on Tue July 2 17:49:41 2019.

@author: Chandan Sharma
"""


from os import listdir
import string
import numpy as np
#from gensim import KeyedVector
#import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords 
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
#from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))


def load_doc(filename):
    file = open(filename, encoding='utf-8')
    text = file.read()
    file.close()
    return text

def split_story(doc):
    index = doc.find('@highlight')
    story, highlights = doc[:index], doc[index:].split('@highlight')
    highlights = [h.strip() for h in highlights if len(h) > 0]
    return story, highlights

def clean_lines(lines):
    cleaned = list()
    table = str.maketrans('', '', string.punctuation)
    for line in lines:
        index = line.find('(CNN) -- ')
        if index > -1:
            line = line[index+len('(CNN)'):]
        line = line.split()
        line = [word.lower() for word in line]
        line = [w.translate(table) for w in line]
        line = [word for word in line if word.isalpha() and not word in stop_words]
        cleaned.append(' '.join(line))
    cleaned = [c for c in cleaned if len(c) > 0]
    return cleaned

def load_stories(directory):
    stories = list()
    for name in listdir(directory):
        filename = directory + '/' + name
        #doc = load_doc(filename)
        #story, highlights = split_story(doc)
        story = load_doc(filename)
        if (len(story) >= 5):
            stories.append({'story':story})#, 'highlights':highlights, 'summary':''})
    return stories

directory = 'dataset/stories_text_summarization_dataset_test'
stories = load_stories(directory)

for example in stories:
    example['story'] = clean_lines(example['story'].split('\n'))
    #example['highlights'] = clean_lines(example['highlights']) 

import numpy as np
word_embeddings = {}
f = open(r'glove.6B.100d.txt', encoding='utf-8')
for line in f:
    values = line.split()
    #print(values)
    word = values[0]
    #print(word)
    coefs = np.asarray(values[1:], dtype='float32')
    #print(coefs)
    word_embeddings[word] = coefs
f.close()

c=0
for j in range(0,len(stories)):
     sentence_vectors = []
     for k in range(0,len(stories[j]['story'])):
         for i in range(0,len(stories[j]['story'][k])):
             if len(stories[j]['story'][k]) != 0:
                 v = sum([word_embeddings.get(w, np.zeros((100,))) for w in stories[j]['story'][k].split()])/(len(stories[j]['story'][k].split())+0.001)
                 c=c+1;
             else:
                 v = np.zeros((100,))
                 c=c+1
         sentence_vectors.append(v)
     sim_mat = np.zeros([len(stories[j]['story']), len(stories[j]['story'])])
     for p in range(len(stories[j]['story'])):
         for q in range(len(stories[j]['story'])):
             if p != q:
                 sim_mat[p][q] = cosine_similarity(sentence_vectors[p].reshape(1,100), sentence_vectors[q].reshape(1,100))[0,0]
     #print(sim_mat)
     nx_graph = nx.from_numpy_array(sim_mat)
     scores = nx.pagerank(nx_graph)
     ranked_sentences = sorted(((scores[h],s) for h,s in enumerate(stories[j]['story'])), reverse=True)
     #print(ranked_sentences[0][1],type(ranked_sentences[0][1]))
     sn = 2
     summ = ''
     #Generate summary
     for o in range(sn):
         summ = summ + ' @highlight ' + str(ranked_sentences[o][1])
         #summ = summ + str(ranked_sentences[o][1]) + '. ' 
         #stories[j]['summary'] = summ
     print('*****', j+1, '*****')
     print (summ)
