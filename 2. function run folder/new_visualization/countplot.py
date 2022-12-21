import matplotlib.pyplot as plt
import pandas as pd

#songs count한 csv 파일 불러오기
df1 = pd.read_csv('new_2019.csv', header=None)
df2 = pd.read_csv('new_2020.csv', header=None)

#기본틀 생성
fig = plt.figure()
axes1 = fig.add_subplot(1,1,1)
axes2 = fig.add_subplot(1,1,1)

#2019년 히스토그램 그래프 만들기(변수1개)
axes1.bar(df1['cnt'], bins = 11) # bins는 x축 간격 조정
#제목
axes1.set_title('cnt_2019')
#x축 라벨링
axes1.set_xlabel('count')
#y축 라벨링
axes1.set_ylabel('songs')

#2020년 히스토그램 그래프 만들기(변수1개)
axes2.bar(df2['cnt'], bins = 11) # bins는 x축 간격 조정
#제목
axes2.set_title('cnt_2020')
#x축 라벨링
axes2.set_xlabel('count')
#y축 라벨링
axes2.set_ylabel('songs')

plt.show()
