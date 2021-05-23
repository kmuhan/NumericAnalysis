from keras.models import Sequential
from keras.layers import Dense
import keras
import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt
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

x = np.array(weight[:400])
y = np.array(longevity[:400])

x_test = np.array(weight[400:])
y_test = np.array(longevity[400:])

W = [1]
b = [1]
H = W*x + b

loss = tf.reduce_mean(tf.square(H - y))

model = Sequential()
model.add(Dense(1, input_dim=1, activation='relu'))

#sgd = keras.models.optimizer_v1.sgd()

model.compile(loss='mse', optimizer='sgd', metrics=['mse'])
model.fit(H, y, epochs=1000, batch_size=5)

#mse = model.evaluate(H, y, batch_size=10)

W, b = model.get_weights()
print(W, b)

plt.scatter(x, y, label='original data')
plt.plot(x, model.predict(x), 'r-', label='fitted line')
plt.plot(x_test, y_test, 'o', color='orange', label='test data')
plt.xlabel('log_{10}(weight)')
plt.ylabel('log_{10}(longevity)')
plt.grid()
plt.title('Keras Sequential')
plt.legend()

print('mse : ', MSE(y_test, W*x_test+b))
plt.show()