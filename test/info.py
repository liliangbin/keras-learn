import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Dense
from keras.models import Sequential

x_data = np.random.rand(100)
noise = np.random.normal(0, 0.01, x_data.shape)
y_data = x_data * 0.1 + 0.2 + noise
plt.scatter(x_data, y_data)
plt.show()

model = Sequential()
model.add(Dense(units=1,input_dim=1))
model.compile(optimizer='sgd', loss='mse')

for step in range(30000):
    # 每次都训练一个批次，这个地方我们使用的是全部放入
    cost = model.train_on_batch(x_data, y_data)
    if step % 500 == 0:
        print('cost:', cost)

w, b = model.layers[0].get_weights()
print('w:', w, 'b:', b)

# x 输入到网络中 得到预测的值
y_pred = model.predict(x_data)

# 显示随机点
plt.scatter(x_data, y_data)
# 显示预测结果
plt.plot(x_data, y_pred, 'r-', lw=3)
plt.show()
