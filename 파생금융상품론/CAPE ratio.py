import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime

# 데이터 소스 설정 및 날짜 범위 정의
start = datetime.datetime(2000, 1, 1)
end = datetime.datetime.now()

# S&P Case-Shiller U.S. National Home Price Index 데이터 가져오기
df = pdr.get_data_fred('CSUSHPINSA', start, end)

print(f'the latest ratio of CAPE ratio : {df.tail(20)}')

# 데이터 시각화
plt.figure(figsize=(12, 7))
plt.plot(df.index, df['CSUSHPINSA'], label='Case-Shiller Home Price Index')
plt.title('S&P/Case-Shiller U.S. National Home Price Index Over Time')
plt.xlabel('Year')
plt.ylabel('Index Value')
plt.legend()
plt.grid(True)
plt.show()


