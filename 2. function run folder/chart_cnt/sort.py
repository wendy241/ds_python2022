# ##오름차순으로 엑셀 정렬

import pandas as pd

data = pd.read_excel('2019.xlsx')
data = data.sort_values(by = 'cnt', ascending=False)

with pd.ExcelWriter('new_2019.xlsx') as writer:
    data.to_excel(writer, sheet_name='sheet1', index=False)

# cnt(각 횟수)를 컬럼으로, 그에 해당하는 노래를 하나의 인스턴스로

##
import pandas as pd

df = pd.read_excel("new_2019.xlsx")

for i in range(14):
    df.fillna('-', inplace = True)

with pd.ExcelWriter('new(2)_2019.xlsx') as writer:
    df.to_excel(writer, sheet_name='sheet1', index=False)
