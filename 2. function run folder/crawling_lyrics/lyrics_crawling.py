import selenium
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
import pandas as pd
from bs4 import BeautifulSoup
#import requests
from itertools import repeat

#차트 파인더 내에 월을 선택하는 div의 xpath가 중간 부분에서 숫자만 다른 주소라, 12달을 모두 리스트화하여, 인덱스값으로 불러오도록 함.
month = ['//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[1]/span/label', '//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[2]/span/label','//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[3]/span/label',
'//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[4]/span/label', '//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[5]/span/label', '//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[6]/span/label',
'//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[7]/span/label', '//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[8]/span/label', '//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[9]/span/label', 
'//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[10]/span/label', '//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[11]/span/label', '//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[12]/span/label'
]

#기존에 수작업으로 행했던 가사 세부정보 버튼에 대한 span주소 100개
f = open('XPath.txt')
full_XPath = f.readlines

result_df = pd.DataFrame()

for j in range(0,12):
    for i in range(0,100):

        driver = wd.Chrome('chromedriver.exe')
        driver.maximize_window()

        url = 'https://www.melon.com/chart/index.htm'
        driver.get(url)

        ##차트파인더 클릭
        driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/div/div/button/span').click()
        ##월간차트 클릭
        driver.find_element(By.XPATH, '//*[@id="d_chart_search"]/div/h4[2]/a').click()
        time.sleep(2)
        ##연대선택 2010년 클릭
        driver.find_element(By.XPATH, '//*[@id="d_chart_search"]/div/div/div[1]/div[1]/ul/li[2]/span/label').click()
        time.sleep(2)
        ##연대선택 2019년 클릭
        driver.find_element(By.XPATH, '//*[@id="d_chart_search"]/div/div/div[2]/div[1]/ul/li[1]/span/label').click()
        time.sleep(2)
        ##월선택
        driver.find_element(By.XPATH, month[j]).click()  # li[j]
        time.sleep(2)
        ## 장르선택 종합 클릭
        driver.find_element(By.XPATH, '//*[@id="d_chart_search"]/div/div/div[5]/div[1]/ul/li[1]/span/label').click()
        time.sleep(2)
        ## 검색버튼 클릭
        driver.find_element(By.XPATH, '//*[@id="d_srch_form"]/div[2]/button/span/span').click()
        time.sleep(2)
        # 상세정보 클릭
        driver.find_element(By.XPATH, full_XPath[i]).click()  # tr[i]값이 다름
        time.sleep(2)
        # 가사 더보기 클릭
        driver.find_element(By.XPATH, '//*[@id="lyricArea"]/button').click()
        time.sleep(2)

        #html 정보 가져오기
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        # 가사 div 카피
        soup.find_all('div', attrs={'class':'lyric on'})
        lyrics_list = [lyrics.get_text() for lyrics in soup.find_all('div', attrs={'class':'lyric on'})]



        df = pd.DataFrame({'lyrics': lyrics_list})
        result_df = pd.concat([result_df, df], ignore_index=True)
        
        

result_df.to_csv('crawling_ly.csv', encoding='ANSI')
