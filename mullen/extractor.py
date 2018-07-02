import os
import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten

class Extractor():
    def __init__(self, input_shape):
        self.model = Sequential()
        
        self.model.add(
            Conv2D(32, (3, 3), activation='relu', input_shape=input_shape)
        )
        
        self.model.add(
            MaxPooling2D(pool_size=(2, 2), strides=(2, 2))
        )

        self.model.add(
            Conv2D(32, (3, 3), activation='relu')
        )
        
        self.model.add(
            MaxPooling2D(pool_size=(2, 2), strides=(2, 2))
        )

        self.model.add(
            Conv2D(16, (3, 3), activation='relu')
        )
        
        self.model.add(
            MaxPooling2D(pool_size=(2, 2), strides=(2, 2))
        )
        
        self.model.add(
            Flatten()
        )
    
    def extract(self, data):
        return self.model.predict(data)
    