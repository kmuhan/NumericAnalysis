import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from ast import literal_eval

weight = []
longevity = []

def MSE(y, pred):
  return np.mean(np.square(y - pred))

with open('data9_avg_avg.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    for line in file:    # for에 파일 객체를 지정하면 파일의 내용을 한 줄씩 읽어서 변수에 저장함
        p = line.strip('\n')
        weight.append(np.log10(float(eval(p)['weight'])))
        longevity.append(np.log10(float(eval(p)['longevity'])))
        #longevity.append(literal_eval(line)['longevity'])

x=np.array(weight)
y=np.array(longevity)

x_test = np.array(weight)
y_test = np.array(longevity)
n=np.size(x)

b=(n*np.sum(x*y)-(np.sum(x)*np.sum(y)))/(n*np.sum(x** 2)-(np.sum(x))**2)
# b= -0.30285714285714288: slope
a=(np.sum(y)-b*np.sum(x))/n
# 0.75714285714285723: intercept
p1=np.polyfit(x,y,1) # 1: linear array([-0.30285714, 0.75714286]) slope and intercept
print(p1)

#plt.scatter(x, y, label='original data')
plt.plot(x, p1[0]*x+p1[1], 'r-', label='fitted line')
plt.plot(x_test, y_test, 'o', label='original_data')
plt.xlabel('log_{10}(weight)')
plt.ylabel('log_{10}(longevity)')
plt.grid()
plt.title('data9_avg_avg')
plt.legend()
print(MSE(y_test,  p1[0]*x_test+p1[1]))

plt.show()