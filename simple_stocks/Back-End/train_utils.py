import os
import csv
import pandas as pd
import numpy as np
import pickle         
import matplotlib.pyplot as plt

from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import validation_curve
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib 




#TICKER = "A"               # change ticker for each stock      

#DATA_ROOT = os.getcwd()

#ADJ_PATH = DATA_ROOT + "/historical_data/"
#ADJ_FILE = TICKER + ".csv"
#ADJ_URL = ADJ_PATH + ADJ_FILE

#MODEL_PATH = DATA_ROOT + "/models/"
#MODEL_FILE = TICKER + "_svr.sav"
#MODEL_URL = MODEL_PATH + MODEL_FILE

class Trainning_Utils:

    # Cross Validation Score
    def cross_val_scores(estimator, X, y):
        scores = cross_val_score(estimator=estimator,
                                 X=X,
                                 y=y,
                                 cv=10)
        print(scores)
    
    
    
    # Validation Curve
    def plot_val_curve(estimator, param_name, X, y):
        param_range = [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]
        train_scores, test_scores = validation_curve(
                        estimator=estimator, 
                        X=X, 
                        y=y, 
                        param_name=param_name, 
                        param_range=param_range,
                        cv=10)
        
        train_mean = np.mean(train_scores, axis=1)
        train_std = np.std(train_scores, axis=1)
        test_mean = np.mean(test_scores, axis=1)
        test_std = np.std(test_scores, axis=1)
        
        plt.plot(param_range, train_mean, 
                 color='blue', linestyle=':',
                 marker='o', markersize=5,
                 label='Training Accuracy')
        
        plt.fill_between(param_range, train_mean + train_std,
                         train_mean - train_std, alpha=0.15,
                         color='blue')
        
        plt.plot(param_range, test_mean, 
                 color='green', linestyle='--', 
                 marker='s', markersize=5, 
                 label='Validation Accuracy')
        
        plt.fill_between(param_range, 
                         test_mean + test_std,
                         test_mean - test_std, 
                         alpha=0.15, color='green')
        
        plt.grid()
        plt.xscale('log')
        plt.legend(loc='lower right')
        plt.xlabel('Parameter Values')
        plt.ylabel('Accuracy')
        plt.ylim([0.8, 1.0])
        plt.tight_layout()
        # plt.savefig('./figures/validation_curve.png', dpi=300)
        plt.show()
    
        
        
        
    # Load the model from disk 
    def load_data_pickle(model_url):
        loaded_model = pickle.load(open(model_url, 'rb'))
        
        return loaded_model
    
    
    
    
    # Save trained model 
    def save_model_pickle(estimator, model_url):             
        save_it = model_url
        pickle.dump(estimator, open(save_it, 'wb'))
     
           
     
    
    
    
    
        
        
    
