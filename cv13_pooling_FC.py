from keras.models import Sequential  #用來啟動 NN
from keras.layers import Conv2D  # Convolution Operation
from keras.layers import MaxPooling2D # Pooling
from keras.layers import Flatten, GlobalAveragePooling2D
from keras.layers import Dense # Fully Connected Networks
input_shape = (32, 32, 3)

model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3), strides=(2,2), padding='same',input_shape=input_shape))
model.add(MaxPooling2D(pool_size = (2, 2)))  ##pooling_size=2,2 strides=2,2 輸出feature map 大小為多少？
model.add(Conv2D(32, kernel_size=(3, 3), strides=(2,2), padding='same',input_shape=input_shape))
model.add(MaxPooling2D(pool_size = (1, 1)))  ##pooling_size=2,2 strides=1,1 輸出feature map 大小為多少？
model.add(Conv2D(10, kernel_size=(3, 3), strides=(2,2), padding='same'))
model.add(Flatten()) ##Flatten完尺寸如何變化？
# model.add(GlobalAveragePooling2D()) #關掉Flatten，使用GlobalAveragePooling2D，完尺寸如何變化？
model.add(Dense(units = 28,activation = 'relu')) ##全連接層使用28個units
print(model.summary())