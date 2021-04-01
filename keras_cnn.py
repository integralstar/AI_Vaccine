import numpy as np
import random
import imutils
import glob
import os
import cv2

from PIL import Image
from keras.utils import np_utils, to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Flatten, Dense, Dropout, LeakyReLU
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import img_to_array
from keras.callbacks import ModelCheckpoint, EarlyStopping

import sklearn.metrics as metrics
from sklearn.metrics import classification_report

IMG_SIZE = 32

class CNN():
    def image_preprocess(self):
        data = []
        labels = []

        Normal_ImagePath = sorted(list(glob.glob('../images/normal/*.png')))

        for Normal_Image in Normal_ImagePath:
        	image = cv2.imread(Normal_Image)
        	image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
        	image = img_to_array(image)
        	data.append(image)
        	labels.append(0) # normal image

        Malware_ImagePath = sorted(list(glob.glob('../images/malware/*.png')))

        for Malware_Image in Malware_ImagePath:
        	image = cv2.imread(Malware_Image)
        	image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
        	image = img_to_array(image)
        	data.append(image)
        	labels.append(1) # malware image

        # scale the raw pixel intensities to the range [0, 1]
        data = np.array(data, dtype="float") / 255.0
        labels = np.array(labels)
        # partition the data into training and testing splits using 75% of
        # the data for training and the remaining 25% for testing
        (train_images, test_images, train_labels, test_labels) = train_test_split(data,
        	labels, test_size=0.20, random_state=7)
        # convert the labels from integers to vectors
        train_labels = to_categorical(train_labels, num_classes=2)
        test_labels = to_categorical(test_labels, num_classes=2)

        self.train_images = train_images
        self.test_images = test_images
        self.train_labels = train_labels
        self.test_labels = test_labels

    def do_cnn(self):

        cnn = Sequential()
        cnn.add(Conv2D(filters=32,
                       kernel_size=(2,2),
                       strides=(1,1),
                       padding='same',
                       input_shape=(IMG_SIZE,IMG_SIZE,3),
                       data_format='channels_last'))
        cnn.add(Activation('relu'))
        cnn.add(MaxPooling2D(pool_size=(2,2),
                             strides=2))
        cnn.add(Conv2D(filters=64,
                       kernel_size=(2,2),
                       strides=(1,1),
                       padding='same'))
        cnn.add(Activation('relu'))
        cnn.add(MaxPooling2D(pool_size=(2,2),
                             strides=2))
        cnn.add(Conv2D(filters=128,
                       kernel_size=(2,2),
                       strides=(1,1),
                       padding='valid'))
        cnn.add(Activation('relu'))
        cnn.add(MaxPooling2D(pool_size=(2,2),
                             strides=2))
        cnn.add(Flatten())
        cnn.add(Dense(128, activation='relu'))
        cnn.add(Dropout(0.4))
        cnn.add(Dense(2, activation='softmax'))
        cnn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        cnn.summary()

        #callback
        checkpointer = ModelCheckpoint('{epoch:04d}.hdf5', save_best_only=True)
        early_stop = EarlyStopping(monitor='loss', patience=7, verbose=1, mode='auto')


        pred = cnn.fit(self.train_images, self.train_labels, epochs=1000, batch_size=100, callbacks=[checkpointer, early_stop])

        #y_pred_labels = np.argmax(pred, axis=1)
        #confusion_matrix = metrics.confusion_matrix(y_true_labels, y_pred_labels)

        loss, acc = cnn.evaluate(self.test_images, self.test_labels, batch_size=100, verbose = 1)
        #print("loss : %s, accuracy : %s" % (loss, acc))
        cnn.save('omega_cnn.h5')

        return loss, acc

        return acc
