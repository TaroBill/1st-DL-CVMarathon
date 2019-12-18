from keras.models import Sequential  #用來啟動 NN
from keras.layers import Conv2D  # Convolution Operation
from keras.layers import MaxPooling2D # Pooling
from keras.layers import Flatten
from keras.layers import Dense # Fully Connected Networks
from keras.layers import BatchNormalization
from keras.layers import Activation
input_shape = (32, 32, 3)

model = Sequential()

##  Conv2D-BN-Activation('sigmoid') 

#BatchNormalization主要參數：
#momentum: Momentum for the moving mean and the moving variance.
#epsilon: Small float added to variance to avoid dividing by zero.

model.add(Conv2D(32,kernel_size=(3,3),strides=(1,1),padding='same',input_shape=input_shape))
model.add(BatchNormalization(name='batch_normalization_1')) 
model.add(Activation('sigmoid'))


##、 Conv2D-BN-Activation('relu')
model.add(Conv2D(32,kernel_size=(3,3),strides=(1,1),padding='same',input_shape=input_shape))
model.add(BatchNormalization(name='batch_normalization_2'))
model.add(Activation('relu'))


print(model.summary())