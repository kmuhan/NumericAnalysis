import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from sklearn.linear_model import LinearRegression
import time

def MSE(y, pred):
  return np.mean(np.square(y - pred))


weight = []
longevity = []

with open('data6_max_avg.txt', 'r') as file:
    for line in file:
        p = line.strip('\n')
        weight.append(np.log10(float(eval(p)['weight'])))
        longevity.append(np.log10(float(eval(p)['longevity'])))

x=np.array(weight[:400]).reshape(-1, 1)
y=np.array(longevity[:400])

x_test = np.array(weight[400:]).reshape(-1, 1)
y_test = np.array(longevity[400:])

# 모델 클래스를 불러오기
lr = LinearRegression()
# 문제와 답을 건네줘서 학습
tic = time.perf_counter()
lr.fit(x,y)
toc = time.perf_counter()

# 테스트를 위해 x값을 줘서 예측해보기
predicted = lr.predict(x)

##그래프로 시각화해보기
plt.scatter(x, y, label='original data')
plt.plot(x, predicted, 'r-', label='fitted line')
plt.plot(x_test, y_test, 'o', color='orange', label='test data')
plt.xlabel('log_{10}(weight)')
plt.ylabel('log_{10}(longevity)')
plt.grid()
plt.title('Scikit-learn LinearRegression')
plt.legend()
# plt.plot(x, y, 'o')
# plt.plot(x, predicted)
print(f'y =  [{lr.coef_}]x + [{lr.intercept_}]')
print(f'MSE = {MSE(y_test, lr.coef_*x_test+lr.intercept_)}, Elapsed time = {(toc - tic) * 1000} milliseconds')
plt.show()