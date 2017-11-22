from collections import defaultdict
from gensim import corpora, models, similarities

with open('./Roy_VnTokenizer-master/scripts/output3.txt') as f:
    mylist = f.read().splitlines()

with open('./stopwords.txt') as f:
    stop_words = f.read().splitlines()

texts = [[word for word in doc.split(' ') if word not in stop_words]
         for doc in mylist]

frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
         for text in texts]

'''remove empty list'''
texts = [x for x in texts if x]

#for t in texts:
#    print(t)

dictionary = corpora.Dictionary(texts)
dictionary.save('./word_dict.dict')  # store the dictionary, for future reference

#print(dictionary)

#print(dictionary.token2id)

corpus = [dictionary.doc2bow(text) for text in texts]

corpora.MmCorpus.serialize('./dict/corpus.mm', corpus)

print(corpus)