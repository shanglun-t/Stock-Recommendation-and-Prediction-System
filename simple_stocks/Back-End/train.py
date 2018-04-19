### Taining new models and saving trained models ###

### Taining new models and saving trained models ###

import os
import csv
import pandas as pd
import numpy as np
import pickle
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})  
np.set_printoptions(suppress=True)

class modelUpdate:
    
    DATA_ROOT = os.getcwd()
    DATA_PATH = DATA_ROOT + "/historical_data/"
    MODEL_PATH = DATA_ROOT + "/models/"
    RESULT_PATH = DATA_ROOT + "/pred_results/"
    
    
    def __init__(self, model=None, pred_result=None):
        pass
    
    def trained_models(self):
        
        with open(DATA_ROOT + "workbook3.csv") as csvfile: 
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            for row in reader:
            tickers = list(row[0])
            
            
        for model in tickers:
            
            MODEL_FILE = TICKER + "_svr.sav"
            MODEL_URL  = MODEL_PATH + MODEL_FILE
                      
            # Load data
            stock_df = pd.read_csv(ADJ_URL, usecols=["Date", "Adj Close"], parse_dates=["Date"]); 
                
            X = stock_df.iloc[:, 0].values  # "Date"
            y = stock_df.iloc[:, 1].values  # "Adj Close"
            
            # Reshape the data array into a 1D numpy array 
            X = np.ndarray.reshape(X, (len(X), 1))
            y = np.ravel(y)
            
            # scaling "Date" array
            sc_X = StandardScaler()
            X = sc_X.fit_transform(X)
                  
            # Train-Test split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)
                    
                    
            # Training models in RBF kernel  C=100, Gamma=100
            model = SVR(kernel='rbf', C=1000, epsilon=0.001, gamma=1000)
                
            #svr_rbf.fit(X_train, y_train)
            model.fit(X_train, np.ravel(y_train,order='F'))
            
            # save trained model at '/models/' 
            pickle.dump(model, open(MODEL_URL, 'wb'))
            
    
    
    def get_results(self, modle=model, X=X_test):
        
        with open(DATA_ROOT + "workbook3.csv") as csvfile: 
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            for row in reader:
            tickers = list(row[0])
            
            
        for file in tickers:
            
            RESULT_FILE = TICKER + "_res.csv"
            RESULT_URL = RESULT_PATH + RESULT_PATH
            
            # model fits test set and get result 
            y_pred_rbf= svr_rbf.predict(X_test)
            
            # save predicted prices into .csv files at '/pred_result/'
            np.savetxt(RESULT_URL, y_pred_rbf, fmt='%1.2f', delimiter=',', header='pred')
            
           
    

