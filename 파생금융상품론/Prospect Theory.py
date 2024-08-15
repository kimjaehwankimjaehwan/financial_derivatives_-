import numpy as np

def prospect_utility(x, alpha=0.5, beta=0.5, gamma=2):
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

# 예시 사용
print("이득 10의 효용:", prospect_utility(10))
print("손실 -5의 효용:", prospect_utility(-5))
