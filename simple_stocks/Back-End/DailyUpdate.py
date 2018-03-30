<<<<<<< HEAD
import csv
=======
import csv 
>>>>>>> 564850d547b22da8f2fff1a2f2fd569ee6eb5fab
import sys
from collections import OrderedDict
import numpy as np
import scipy as sp
import os
from functools import reduce
import string

count = 0

<<<<<<< HEAD
sumOfClose = np.array([])
directory = os.path.join("Users/jayb/Desktop/srps/", "historical_data")
for root, dirs, files in os.walk("historical_data"):
    for file in files:
        if file.endswith(".csv"):
=======

sumOfClose = np.array([])
directory = os.path.join("Users/jayb/Desktop/srps/", "historical_data")
for root, dirs,files in os.walk("historical_data"):
    for file in files:
       if file.endswith(".csv"):
>>>>>>> 564850d547b22da8f2fff1a2f2fd569ee6eb5fab
            with open(os.path.join(root, file)) as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                next(reader)
                adjReturn = np.array([])
                for row in reader:
                    try:
<<<<<<< HEAD
                        adj = (next(reader))
                        adj = float(adj[5])
                        adjReturn = np.append(adjReturn, (float(row[5]) / adj - 1))
                    except:
                        pass
                # simpleReturn = (closePrice[-1] - closePrice[0])/closePrice[0]
                # annualReturn = (simpleReturn + 1)**((1 / 10)-1)

                sector = None
                industry = None

                with open("workbook3.csv") as csvfile:
                    reader1 = csv.reader(csvfile, delimiter=',')
                    next(reader1)
                    file = file[0:-4]

                    for row in reader1:
                        if row[0] == file:
                            company = row[1]
                            sector = row[2]
                            industry = row[3]

                try:
                    row = '\n' + str(file) + ', ' + str(company) + ', ' + str(sector) + ', ' + str(
                        industry) + ', ' + str(np.std(adjReturn)) + ', ' + str(np.var(adjReturn)) + ', ' + str(
                        np.mean(adjReturn))
                except:
                    pass
                fd = open('industry_performance.csv', 'a')
                fd.write(row)
                count = count + 1
                fd.close()

                # sumOfClose = np.append (sumOfClose, np.std(closePrice))
                closePrice = None
print(count)
=======
                         adj = (next(reader))
                         adj = float(adj[6])
                         adjReturn = np.append (adjReturn, (float(row[6])/adj -1 ))
                    except:
                        pass
                #simpleReturn = (closePrice[-1] - closePrice[0])/closePrice[0]
                #annualReturn = (simpleReturn + 1)**((1 / 10)-1)

                sector = None
                industry = None
                
                with open("workbook4.csv") as csvfile:
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
>>>>>>> 564850d547b22da8f2fff1a2f2fd569ee6eb5fab
