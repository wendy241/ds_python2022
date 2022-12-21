import pandas as pd
import csv
#from xlutils.copy import copy

file_list = ['202003.csv', '202004.csv', '202005.csv', '202006.csv', '202007.csv', '202008.csv']
file_list2 = ['202009.csv', '202010.csv', '202011.csv', '202012.csv', '202101.csv', '202102.csv']

singer = []
song = []
##1. 1년치의 모든 노래 및 가수 파일을 한 군데로 모을 것.
for j in range(len(file_list)):
    df = pd.read_csv(file_list[j], encoding='utf-8')
    singers = df['가수명']
    singer_val = singers.values
    singer_list = singer_val.tolist()

    songs = df['곡명']
    song_val = songs.values
    song_list = song_val.tolist()

    singer.append(singer_list)
    song.append(song_list)

for j in range(len(file_list2)):
    df = pd.read_csv(file_list[j], encoding = 'utf-8')

    singers = df['가수명']
    singer_val = singers.values
    singer_list = singer_val.tolist()

    songs = df['곡명']
    song_val = songs.values
    song_list = song_val.tolist()

    singer.append(singer_list)
    song.append(song_list)

#
song = tuple(song)
song = tuple(song)

##2. 중복 값 카운트 후 중복 값 제거
def get_counts(song):
    counts = {}
    for x in song:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

counts = get_counts(song)

lst = []
for i in song:
    for j in count:
        if i == j:
            lst.append(count[i])


data = {'song': song, 'cnt':lst}

##3. 카운트 값 엑셀에 추가.
data = pd.DataFrame(data)
data.to_csv('2020.csv')