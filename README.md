# 주제: 코로나로 인한 음원차트의 변화
조번호:6
조원: 김예진, 김현민, 박나예

주제선정이유 및 목적: 

노래는 듣는 사람의 심리를 반영한다. 코로나로 인해 사람들을 만나지 못하고 혼자 격리하는 시간이 많아지자 혼자 음악을 들을 일이 급증했으며 ‘코로나 블루’라는 신조어가 생길 정도로 우울, 울적해지는 기분 또한 잦아졌다. 이러한 변화는 사람들이 듣는 음악에서도 나타날 것, 즉 코로나 전후 음원 트렌드의 변화가 존재할 것이라 생각하였다. 
따라서 코로나 펜데믹으로 인한 음원 트렌드 변화를 파악하기 위해 이 주제를 진행하였다.

상세내용:
- 코로나 바이러스19가 2020년 02월에 시작되었으므로 2020년 02월을 기준으로 하여 1년 전후로 월별차트를 수집한다.
- 즉 2019년 03월 월간차트부터 2020년 02월 월간차트를 코로나 전, 2020년 03월 월간차트부터 2021년 02월 월간차트를 코로나 후로 설정
방법:(주의해야할 점 및 코드 예시)
- 2년치 멜론월별 음원차트를 크롤링해 가수, 곡명, 가사 등 필요한 자료들 수집
>> ’201901~06chart.py’, ’201907~12chart.py’, ’202001~06chart.py’, ’202007~12chart.py’
>> 작년 크롤링할 때 사용했던 find_all() 함수가 이제는 사용이 되지 않음에 따라 find_element() 함수를 이용한 코드로 재수정하여 클릭하고자 했던 버튼에 접근했다.
- 차트 유동성 유무 파악
>> ’2019_chart_cnt.py’, ’2020_chart_cnt.py’, ’sort.py’
- 가사 내 특정 단어 노출 횟수 파악
>>’lyrics_crawling.py’
>>멜론 차트의 작업자 모드에서 세부 가사를 파악하기 위해 필요한 span의 x_path가 모든 노래에 대해 동일한 주소를 가지고 있고, 화면 상 뒤로 가기를 누르면 초기화되는 차트파인더에 대해 크롬드라이버의 접근이 불가해져서 수작업으로 진행했던 작업에 대해 full x_path에서 다른 주소를 찾아내어 반복문을 통해 크롤링할 수 있는 코드를 새로 작성했다.

시각화자료:
- 코로나 이후 시기 음원차트가 이전 차트보다 고정적이었음
![image](https://user-images.githubusercontent.com/84655628/208857357-b660ad58-f61e-4100-9b96-9d6894794d12.png)

- 이지리스닝 노래들을 더 많이 들었음

![image](https://user-images.githubusercontent.com/84655628/208857391-90ebf46d-4dc5-4e70-b6f1-660b849b59ee.png)

<2019년 3월부터 2020년 2월까지 12번 차트에 오른 노래가사 내 단어 노출 수에 대한 크롤링에 대한 워드클라우드>

![image](https://user-images.githubusercontent.com/84655628/208857432-2d98c89a-43f3-4fa1-a303-d23dcd48a17e.png)

<2020년 3월부터 2021년 2월까지 12번 차트에 오른 노래가사 내 단어 노출 수에 대한 크롤링에 대한 워드클라우드>

기존 진도 대비 추가 개발된 정도:
1) 2019년, 2020년 각각의 순위에 랭크된 노래 재목만 추출하여 형태소분석 후에 명사만 따냄. 각 연도별로 제목의 명사 총 빈도수를 matplotlib으로 시각화
>> 2. funcion run folder - title_cnt - title_barchart.py 실행하면 된다

2) matplotlib을 사용하여 count된 차트들을 bar graph로 시각화
>> 2. function run folder - new_visualization - countplot.py 실행하면 된다

각 repositery 내에 있는 test는 파일을 생성하기 위한 빈파일입니다.
