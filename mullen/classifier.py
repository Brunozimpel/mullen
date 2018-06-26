from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.utils import to_categorical
from keras.models import load_model
from mullen.extractor import Extractor
import mullen.video as vd
import numpy as np
import pickle
import json
import os


class Mullen():
    def __init__(self, frame):
        self.downsample_size=40
        self.extractor = Extractor(input_shape=frame)
        self.data_pkl = 'cache/X_Y_classes.pkl'

    def session(self, data_dir, **kwargs):
        if not os.path.exists('cache'):
            os.makedirs('cache')
            
        if not os.path.exists(self.data_pkl):
            print("Loading data from %s" % data_dir)  

            X, Y = self._load_data(data_dir)
            Y = to_categorical(Y,self.num_classes)
            
            print('Saving to %s' % self.data_pkl)
            with open(self.data_pkl, 'wb') as f:
                pickle.dump((X,Y,self.classes), f)    
        else:
            print("Loading from data from %s" % self.data_pkl)
            with open(self.data_pkl, 'rb') as f:
                X, Y, self.classes = pickle.load(f)
        
        input_shape=X[0].shape
        self.num_classes = Y.shape[1]
        print("Creating lstm with shape = %s and %i classes" 
              % (str(input_shape), self.num_classes))
        self.model = self._lstm(input_shape, self.num_classes)

        self.model.fit(X, Y, **kwargs)
        
    def guess_trick(self, data):
        processed = self._pipeline(data)
        self.last_prediction = self.model.predict(np.expand_dims(processed,axis=0))
        return self.classes[np.argmax(self.last_prediction)]
    
    def load_session(self, path):
        print('Loading saved model at %s' % path)
        self.model = load_model(path+'model.h5')
        with open(path+'classes.pkl', 'rb') as f:
            self.classes = pickle.load(f)
        print(self.classes)
        
    def save_session(self, path):
        try:
            os.makedirs(path)
        except:
            print('Model already exits!')
        else:
            print('Saving saved model at %s' % path)

            self.model.save(path+'model.h5')

            with open(path+'classes.pkl', 'wb') as f:
                pickle.dump(self.classes, f)  
        
    def _lstm(self, input_shape, num_classes):        
        model = Sequential()
        model.add(LSTM(32, return_sequences=True,input_shape=input_shape))
        model.add(LSTM(32, return_sequences=True))  
        model.add(LSTM(32))  
        model.add(Dense(num_classes, activation='softmax'))

        model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
        
        return model                
              
    def _load_data(self, data_dir):    
        classes = os.listdir(data_dir)
        self.classes = {i:classes[i] for i in range(len(classes))}
        self.num_classes = len(self.classes)
        for k,v in self.classes.items():        
            # Selects the directory of the current class
            cur_dir = data_dir+self.classes[k]+'/'

            # list the videos in the current dir
            videos = os.listdir(data_dir+self.classes[k])
            videos = [cur_dir+vid for vid in videos]
            size = len(videos)

            print("%i videos from %s" % (size, cur_dir))

            x_proc = np.array(list(map(self._pipeline, videos)))
            y_proc = np.ones(size).reshape(-1,1)*k

            if k == 0: #First iteration
                X = x_proc
                Y = y_proc
            else:
                X = np.vstack((X,x_proc))
                Y = np.vstack((Y,y_proc))    
        print("Shape X =", X.shape)
        print("Shape Y =", Y.shape)

        return X, Y
    
    def _pipeline(self, video):
        return self.extractor.extract(
            vd.downsample(
                vd.video_to_array(video), 
                self.downsample_size
            )/255
        )
            