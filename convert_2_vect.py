from gensim import corpora, models, similarities
import os
from pprint import pprint

if (os.path.exists("./word_dict.dict")):
    dictionary = corpora.Dictionary.load('./word_dict.dict')
    corpus = corpora.MmCorpus('./dict/corpus.mm')

tfidf = models.TfidfModel(corpus)

corpus_tfidf = tfidf[corpus]

lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)

doc  = "Theo tờ báo được cho là thân Real, mùa giải 2011-2012, đội chủ sân Bernabeu có bảy trận ghi nhiều hơn ba bàn. Con số này ở mùa 2012-2013 là bốn, và mùa 2013-2014 là năm lần."
vec_bow = dictionary.doc2bow(doc.lower().split())
vec_lsi = lsi[vec_bow]


index = similarities.MatrixSimilarity(lsi[corpus])

'''search quuery'''
sims = index[vec_lsi]
sims = sorted(enumerate(sims), key=lambda item: -item[1])
pprint(sims)