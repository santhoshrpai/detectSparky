from __future__ import absolute_import
from __future__ import print_function
import numpy as np
import keras
import h5py

np.random.seed(1337)  # for reproducibility

author = "santhosh"
#Reference: Keras Library
#http://keras.io/
#https://github.com/fchollet/keras/tree/master/examples

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils
import cPickle
import gzip

def load_data(path):
    if path.endswith(".gz"):
        f = gzip.open(path, 'rb')
    else:
        f = open(path, 'rb')

    data = cPickle.load(f)
    f.close()
    return data  # (X, Y)

batch_size = 10
nb_classes = 10
nb_epoch = 1

# input image dimensions
img_rows, img_cols = 256, 384
# number of convolutional filters to use
nb_filters = 32
# size of pooling area for max pooling
nb_pool = 2
# convolution kernel size
nb_conv = 3

# the data, shuffled and split between tran and test sets
# (X_train, y_train), (X_test, y_test) = mnist.load_data()
training_path = "./../data_processing/training_data_10.pkl.gz"
testing_path = "./../data_processing/testing_data_10.pkl.gz"

(X_train, y_train) = load_data(training_path)
(X_test, y_test) = load_data(testing_path)

print(X_train.shape)
print(len(y_train))
print(X_test.shape)
print(len(y_test))


X_train = X_train.reshape(X_train.shape[0], 1, img_rows, img_cols)
X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
X_train = X_train.astype("float32")
X_test = X_test.astype("float32")
X_train /= 255
X_test /= 255
print('X_train shape:', X_train.shape)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)

# Build the model
model = Sequential()

model.add(Convolution2D(nb_filters, nb_conv, nb_conv,
                        border_mode='valid',
                        input_shape=(1, img_rows, img_cols)))
model.add(Activation('relu'))
model.add(Convolution2D(nb_filters, nb_conv, nb_conv))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))

# Compile the model with loss function and optimizer
model.compile(loss='categorical_crossentropy', optimizer='sgd')

# Train the model
model.fit(X_train, Y_train, batch_size=batch_size, nb_epoch=nb_epoch, show_accuracy=True, verbose=1, validation_data=(X_test, Y_test))

#save the model
saved_model = model.to_json()
open('my_model_architecture.json', 'w').write(saved_model)
model.save_weights('model_weights.h5')

# Evaluate the model
score = model.evaluate(X_test, Y_test, show_accuracy=True, verbose=0)

# Print the summary of results
print("Entire Scores")
print(score)
print("==========================================")
print('Test score:', score[0])
print('Test accuracy:', score[1])