import selenium
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
from itertools import repeat

month = ['//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[1]/span/label', '//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[2]/span/label',
         '//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[3]/span/label', '//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[4]/span/label',
         '//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[5]/span/label', '//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[6]/span/label']

filelist = ['202001.csv', '202002.csv', '202003.csv', '202004.csv', '202005.csv', '202006.csv']

result_df = pd.DataFrame()
for j in range(len(month)):

        driver = wd.Chrome('C:\chromedriver.exe')
        driver.maximize_window()

        url = 'https://www.melon.com/chart/index.htm'
        driver.get(url)

        ##차트파인더 클릭
        driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/div/div/button/span').click()
        ##월간차트 클릭
        driver.find_element(By.XPATH, '//*[@id="d_chart_search"]/div/h4[2]/a').click()
        time.sleep(2)
        ##연대선택 2020년대 클릭
        driver.find_element(By.XPATH, '//*[@id="d_chart_search"]/div/div/div[1]/div[1]/ul/li[1]/span/label').click()
        time.sleep(2)
        ##연도선택 2020년 클릭
        driver.find_element(By.XPATH, '//*[@id="d_chart_search"]/div/div/div[2]/div[1]/ul/li[3]/span/label').click()
        time.sleep(2)
        ##월선택 1월클릭
        driver.find_element(By.XPATH, month[j]).click()
        time.sleep(2)
        ## 장르선택 종합 클릭
        driver.find_element(By.XPATH, '//*[@id="d_chart_search"]/div/div/div[5]/div[1]/ul/li[1]/span/label').click()
        time.sleep(2)
        ## 검색버튼 클릭
        driver.find_element(By.XPATH, '//*[@id="d_srch_form"]/div[2]/button/span/span').click()
        time.sleep(2)
        #html 정보 가져오기
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        #soup.find_all함수를 이용해서 ellipsis rank01 class에서 song 이름이 담긴 a태그를 찾아 song_list에 노래제목 넣어주기
        soup.find_all('div', attrs={'class': 'ellipsis rank01'})
        song_list = [title.find('a').get_text() for title in soup.find_all('div', attrs={'class': 'ellipsis rank01'})]

        #soup.find_all함수를 이용해서 ellipsis rank02 class에서 singer 이름이 담긴 a태그를 찾아  singer_list에 가수 이름 넣어주기
        soup.find_all('div', attrs={'class': 'ellipsis rank02'})
        singer_list = [singer.get_text() for singer in soup.find_all('div', attrs={'class': 'ellipsis rank02'})]

        rank_list = []

        for i in range(len(song_list)):
            rank_list.append(i + 1)
        
        #연도와 월별 데이터를 datelk라는 클래스에서 찾아 리스트로 넣어주기
        year_list = list(repeat(soup.find_all('span', attrs={'class': 'datelk'})[0].get_text(), len(song_list)))
        month_list = list(repeat(soup.find_all('span', attrs={'class': 'datelk'})[1].get_text(), len(song_list)))
        
        #위에서 수집한 연도, 월, 순이, 곡명, 가수명 데이터를 데이터 프레임으로 묶어 csv파일로 만들기
        df = pd.DataFrame({'연도': year_list, '월': month_list, '순위': rank_list, '곡명': song_list, '가수명': singer_list})
        result_df = pd.concat([result_df, df], ignore_index=True)

        result_df.to_csv(filelist[j], encoding='utf-8-sig')
        result_df = pd.DataFrame()
        
