import gensim
from pprint import pprint
from gensim.models.keyedvectors import KeyedVectors

with open('./Roy_VnTokenizer-master/scripts/output3.txt') as f:
    mylist = f.read().splitlines()

mylist = [s.split(' ') for s in mylist]

model = gensim.models.Word2Vec(mylist, size=100, window=5, min_count=1)
pprint(model.wv.similar_by_word('khuôn_khổ',topn=3))