import pandas as pd
import sys, os
from konlpy.tag import Kkma, Okt
from collections import Counter
import nltk
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
import warnings
warnings.filterwarnings(action='ignore')


path = 'C:/Users/82108/PycharmProjects/ds_python2022/1.resource.folder/musicrank_crawling/'
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith('.csv')]

df = pd.DataFrame()
for i in file_list_py:
    data = pd.read_csv(path + i, index_col=0)
    df = pd.concat([df, data])

title2019=df[df['연도']==2019]['곡명'].to_list()
title2020=df[df['연도']==2020]['곡명'].to_list()

ok=Okt()
tag2019=[]
for word in title2019:
  morph = ok.pos(word)
  tag2019.append(morph)
tag2020=[]
for word in title2020:
  morph = ok.pos(word)
  tag2020.append(morph)

noun_title2019=[]
for my_sentence in tag2019:
  for word, tag in my_sentence:
    if tag in ['Noun']:
        noun_title2019.append(word)
noun_title2020=[]
for my_sentence in tag2020:
  for word, tag in my_sentence:
    if tag in ['Noun']:
        noun_title2020.append(word)
# kkma=Kkma()
# noun_title2019=kkma.nouns(title2019)
# noun_title2020=kkma.nouns(title2020)

count_noun_title2019=Counter(noun_title2019)
count_noun_title2020=Counter(noun_title2020)

# plt.rc('font',family='NanumBarunGothic')
plt.rcParams['font.family'] = 'Malgun Gothic'

freq_2019=FreqDist(count_noun_title2019)
freq_2020=FreqDist(count_noun_title2020)
freq_2019.plot()
freq_2020.plot()