import numpy as np
import matplotlib.pyplot as plt

def prospect_utility(x, alpha=1, beta=1, gamma=2.5):
    """
    전망 이론의 효용 함수를 계산합니다.

    :param x: 손실 또는 이득
    :param alpha: 이득에 대한 기울기
    :param beta: 손실에 대한 기울기
    :param gamma: 곡률 매개변수
    :return: 효용 값
    """
    if x >= 0:
        return alpha * (x ** gamma)
    else:
        return -beta * ((-x) ** gamma)

# 시각화를 위해 x 범위를 설정합니다.
x_values = np.linspace(-10, 10, 100)
y_values = [prospect_utility(x) for x in x_values]

# 시각화
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='Prospect Utility Function', color='blue')
plt.title('Prospect Utility Function')
plt.xlabel('Outcome')
plt.ylabel('Utility')
plt.grid(True)
plt.legend()
plt.show()
