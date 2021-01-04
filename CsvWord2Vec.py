from konlpy.tag import Okt
from gensim.models import Word2Vec
import pandas as pd
import csv

twitter = Okt()

file = open("output/train.txt",'r', encoding='utf-8')
Line=[]

while True:
    tline = file.readline()
    if not tline: break
    Line.append(tline.rstrip('\n'))

token = []
embeddingmodel = []

f = open("output/train_tag.txt",'r',encoding='utf-8')
key=[]

while True:
    nline = f.readline()
    if not nline: break
    key.append(nline.rstrip('\n'))

cnt = 0
for i in Line:
    li = i.split('\t')
    if len(li) < 2 :
        li = Line[cnt-1].split('\t')
        sentence = twitter.pos(li[1], norm=True, stem=True)
    else:
        sentence = twitter.pos(li[1], norm=True, stem=True)
    temp = []
    temp_embedding = []
    all_temp = []
    for k in range(len(sentence)):
        temp_embedding.append(sentence[k][0])
        temp.append(sentence[k][0] + '/' + sentence[k][1])
    all_temp.append(temp)
    embeddingmodel.append(temp_embedding)
    category = li[0]
    category_number_dic = {string:l for l, string in enumerate(key)}
    all_temp.append(category_number_dic.get(category))
    token.append(all_temp)
    cnt = cnt+1

embeddingmodel = []
for i in range(len(token)):
    temp_embeddingmodel = []
    for k in range(len(token[i][0])):
        temp_embeddingmodel.append(token[i][0][k])
    embeddingmodel.append(temp_embeddingmodel)
embedding = Word2Vec(embeddingmodel, size=300, window=5, min_count=5, iter=2, sg=1)
embedding.save('post.embedding')
