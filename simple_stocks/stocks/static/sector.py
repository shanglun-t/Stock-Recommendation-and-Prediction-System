import csv
import sys
from collections import OrderedDict
import numpy as np
import scipy as sp
import itertools

class SectorSelection:
    

    def __init__(self, holdingPeriod, riskLevel):
        self.holdingPeriod = holdingPeriod
        self.riskLevel = riskLevel



    # returns list of Sector with value in range of high and low
    def reduceByValue(self, low, high, myDict):
        result = list()
        for k, v in myDict.items():
                if float(v) >= low and float(v) <= high:
                    result.append (k)
                    
        return result
    
    # provides list of Sector based on volatility and risk chosen by the user 
    def getSectorList(self):
        sectorVolatility = dict()
        sectorRisk = dict()
        sectorReturn = dict()
        
        
        
        with open('/static/sector_performance.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)

            for row in reader:
                sectorVolatility[row[0]] = row[1]
                sectorRisk[row[0]] = row[2]
                sectorReturn[row[0]] = row[3]
                
        low = min (float(sectorVolatility[k]) for k in sectorVolatility)
        high = max (float(sectorVolatility[k]) for k in sectorVolatility)
        diff = (high - low)/5
                
        print ('RANGE:', diff)
        print (low)

        if self.holdingPeriod == 'T1':
            pass
        if self.holdingPeriod == 'T2':
            low = low + diff 
        if self.holdingPeriod == 'T3':
            low = low + diff * 2
        if self.holdingPeriod == 'T4':
            low = low + diff * 3
        if self.holdingPeriod == 'T5':
            low = low + diff * 4
            
        high = low + diff
        
        result =self.reduceByValue(low, high ,sectorVolatility)

        

        sectorRisk = {k: sectorRisk[k] for k in result if k in sectorRisk}
        print ('list of risk', sectorRisk)

        low = min (float(sectorRisk[k]) for k in sectorRisk)
        high = max (float(sectorRisk[k]) for k in sectorRisk)
        diff = (high - low)/2

        if self.riskLevel == 'R1' or self.riskLevel == 'R2':
            pass
        if self.riskLevel == 'R3' or self.riskLevel == 'R4':
            low = low + diff 
            
        high = low + diff
        
        result =self.reduceByValue(low, high ,sectorRisk)

        

        sectorReturn = {k: sectorReturn[k] for k in result if k in sectorReturn}
        print ('list of return', sectorReturn)

        low = min (float(sectorReturn[k]) for k in sectorReturn)
        high = max (float(sectorReturn[k]) for k in sectorReturn)
        diff = (high - low)/2
            
        high = low + diff
        print (high, 'this is high for return')

        result = list()
        for k, v in sectorReturn.items():
                if float(v) > high:
                    result.append (k)
        
        
        return 'result of return', result


    
                 
class IndustrySelection:
    pass
class StockSelection:
    pass

S1 = SectorSelection ('T2', 'R3')
print (S1.getSectorList())
