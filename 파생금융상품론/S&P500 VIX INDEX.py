import yfinance as yf
import matplotlib.pyplot as plt

# VIX 지수 데이터를 가져옵니다.
vix = yf.Ticker("^VIX")

# 최근 1년간의 일일 VIX 지수 데이터를 다운로드합니다.
vix_data = vix.history(period="2y")

# VIX 지수의 종가를 그래프로 나타냅니다.
plt.figure(figsize=(15, 7))
plt.plot(vix_data.index, vix_data['Close'], label='VIX Close Price')
plt.title('S&P 500 VIX Index - Last 2 Year')
plt.xlabel('Date')
plt.ylabel('VIX Index Value')
plt.legend()
plt.grid(True)
plt.show()
