import csv 
import sys
from collections import OrderedDict
import numpy as np
import scipy as sp
import os
from functools import reduce
import string


count = 0


sumOfClose = np.array([])
directory = os.path.join("/Users/user/Capstone/simple_stocks/static/csv", "historical_data/")
for root, dirs,files in os.walk("historical_data"):
    for file in files:
       if file.endswith(".csv"):
            with open(os.path.join(root, file)) as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                next(reader)
                adjReturn = np.array([])
                for row in reader:
                    try:
                         adj = (next(reader))
                         adj = float(adj[6])
                         adjReturn = np.append (adjReturn, (float(row[6])/adj -1 ))
                    except:
                        pass
                #simpleReturn = (closePrice[-1] - closePrice[0])/closePrice[0]
                #annualReturn = (simpleReturn + 1)**((1 / 10)-1)

                sector = None
                industry = None
                
                with open("/Users/user/Capstone/simple_stocks/static/csv/Workbook3.csv") as csvfile:
                    reader1 = csv.reader(csvfile, delimiter=',')
                    next(reader1)
                    file = file [0:-4]
                    
                    for row in reader1:                                              
                        if row[0]== file:
                            sector = row [2]
                            industry = row[3]
                            
                try:                       
                    row = '\n' + str(file) + ', '+ str(sector) + ', '+ str(industry) + ', '+ str(np.var(adjReturn)) + ', '+ str(np.std(adjReturn)) +', '+ str(np.mean(adjReturn))  
                except:
                    pass
                fd = open('lala.csv','a')   
                fd.write(row)                              
                count = count + 1
                fd.close()
                
                #sumOfClose = np.append (sumOfClose, np.std(closePrice))
                closePrice = None
print (count)
