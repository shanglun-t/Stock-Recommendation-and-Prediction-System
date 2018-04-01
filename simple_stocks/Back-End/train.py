### Taining new models and saving trained models ###

import os
import csv
import pandas as pd
import numpy as np
import pickle

from sklearn.pipeline import Pipeline
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

# To plotting figures
#%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12



TICKER = "A"               # change ticker for each stock 

DATA_ROOT = os.getcwd()

ADJ_PATH = DATA_ROOT + "/historical_data/"
ADJ_FILE = TICKER + ".csv"
ADJ_URL  = ADJ_PATH + ADJ_FILE

MODEL_PATH = DATA_ROOT + "/models/"
MODEL_FILE = TICKER + "_svr.sav"
MODEL_URL  = MODEL_PATH + MODEL_FILE

FIG_PATH = DATA_ROOT + "/figures/"
FIG_FILE = TICKER + "_svr_pred.png"
FIG_URL  = FIG_PATH + FIG_FILE

def main():
    
    # Load data
    stock_df = pd.read_csv(ADJ_URL, usecols=["Date", "Adj Close"], parse_dates=["Date"]); 
        
    X = stock_df.iloc[:, 0].values  # "Date"
    y = stock_df.iloc[:, 1].values  # "Adj Close"
    
    # Reshape the data array into a 1D numpy array 
    X = np.reshape(X, (len(X), 1))
    y = np.reshape(y, (len(y), 1))
    
    
    # scaling "Date" array
    sc_X = StandardScaler()
    
    X = sc_X.fit_transform(X)
    
          
    # Train-Test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)
            
            
    # Training models in RBF kernels  C=100, Gamma=100
    svr_rbf = SVR(kernel='rbf', C=100, epsilon=0.001, gamma=100)
        
    #svr_rbf.fit(X_train, y_train)
    svr_rbf.fit(X_train, np.ravel(y_train,order='F'))
    
    
    # Plotting predictions
    #plt.grid()
    #plt.plot(X, y_pred_lin, color='orange', label='Linear Kernel')
    #plt.plot(X, y_pred_poly, color='green', label='Polynomial Kernel')
    #plt.plot(X, y_pred_rbf, color='blue', label='RBF Kernel')
    #plt.xlabel('Dates')
    #plt.ylabel('Prices')
    #plt.title('Predicted Price Trend')
    #plt.legend()
    #plt.savefig(FIG_URL, dpi=300)
    #plt.show()
    

    
    # Cross Validation Score
    #scores = cross_val_scores(sv_regr, X_train, y_train)
    #print('Cross Validation Score: %s' % scores)
    #print('CV accuracy: %.3f +/- %.3f' % (np.mean(scores), np.std(scores)))
    
    
    
    # Validation Curve
    #param_name='Gamma'    # or param_name='C'
    #plot_val_curve(sv_regr, param_name, X_train, y_train)
    
    
    # Grid-Search CV
    #grid_search_CV(X_train, y_train)
    #regr = gs.best_estimator_
    #regr.fit(X_train, y_train)
    #print('Test accuracy: %.3f' % regr.score(X_test, y_test))
    
    
    
    # save model
    save_model_pickle(svr_rbf, MODEL_URL)


    
if __name__ == '__main__':
    main()
