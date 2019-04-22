import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Dense
from keras.models import Sequential

x_data = np.linspace(-0.5, 0.5, 200)
noise = np.random.normal(0, 0.02, x_data.shape)
y_data = np.square(x_data) + noise
plt.scatter(x_data, y_data)
plt.show()
