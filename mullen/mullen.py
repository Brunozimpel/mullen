from keras.models import Sequential
from keras.layers import LSTM, Dense


class Mullen():
    def __init__(self, timesteps, data_dim, num_classes):       
        
        self.model = Sequential()
        self.model.add(LSTM(32, return_sequences=True,
                       input_shape=(timesteps, data_dim)))  
        self.model.add(LSTM(32, return_sequences=True))  
        self.model.add(LSTM(32))  
        self.model.add(Dense(num_classes, activation='softmax'))
        
        self.model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])        
        
    def session(self, 
        x_train, y_train,
        validation_data,
        batch_size=64, epochs=5)
    
        self.model.fit(x_train, y_train,
          batch_size=batch_size, epochs=epochs,
          validation_data=validation_data)
        
    def guess_trick(self, data)
        return self.model.predict(data)