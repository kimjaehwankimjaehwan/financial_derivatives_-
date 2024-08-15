import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='NanumBarunGothic')
# 엑셀 파일에서 데이터 불러오기
file_path = 'data_3905_20240511.xlsx'  # 파일 경로를 정확히 지정하세요
df = pd.read_excel(file_path)

# '일자' 컬럼을 datetime 형태로 변환
df['일자'] = pd.to_datetime(df['일자'])
recent_data = df[['일자', '정산가']].tail(20)
print(recent_data)

# 데이터 시각화
plt.figure(figsize=(15, 7))
plt.plot(df['일자'], df['정산가'], linestyle='-', color='b', label='정산가')
plt.title('KOSPI200 변동성지수 선물 가격 추이')
plt.xlabel('날짜')
plt.ylabel('정산가')
plt.grid(True)
plt.legend()
plt.show()
