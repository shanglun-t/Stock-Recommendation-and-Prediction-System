import csv 
import sys
from collections import OrderedDict
import numpy as np
import scipy as sp
import os
import stocks.sector
import functools as ft
import stocks.performance


class IndustrySelection:
    
    def __init__(self, holdingPeriod, riskLevel):
        self.holdingPeriod = holdingPeriod
        self.riskLevel = riskLevel
        self. selectedSector = sector.SectorSelection(self.holdingPeriod, self.riskLevel)
        self.selectedSectorList = self.selectedSector.getSectorList()
        
    def getIndustryList (self):


        '''
        selectedSector = sector.SectorSelection(self.holdingPeriod, self.riskLevel)
        selectedSectorList = selectedSector.getSectorList()
        print ('check', selectedSectorList) '''
        
        
        industryVolatility = dict()
        industryRisk = dict()
        industryReturn = dict()
    

        # read csv file and create dictionary for each column
        with open('/Users/user/Capstone/simple_stocks/static/csv/industry_performance.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            
            for row in reader:
                #print (row [1], self.selectedSectorList, row[2], row[3])
                if str(row[1]) in self.selectedSectorList:
                    industryVolatility.setdefault(row[2], []).append(float(row[3]))
                    industryRisk.setdefault(row[2], []).append(float(row[4]))
                    industryReturn.setdefault(row[2], []).append(float(row[5]))


        for k, v in industryVolatility.items():
            industryVolatility[k] = ft.reduce(lambda x, y: x + y, v) / len(v)
        for k, v in industryRisk.items():
            industryRisk [k] = ft.reduce(lambda x, y: x + y, v) / len(v)
        for k, v in industryReturn.items():
            industryReturn [k] = ft.reduce(lambda x, y: x + y, v) / len(v)

        
        
        p1 = performance.SelectionByPerformance(self.holdingPeriod, self.riskLevel, industryVolatility, industryRisk, industryReturn)
        industryList = p1.getPerformanceList() 
        return industryList
    
        

