import csv
import functools as ft
from  .performance import*
from .sector import *


class IndustrySelection:
    
    def __init__(self, holdingPeriod, riskLevel):
        self.holdingPeriod = holdingPeriod
        self.riskLevel = riskLevel
        self. selectedSector = SectorSelection(self.holdingPeriod, self.riskLevel)
        self.selectedSectorList = self.selectedSector.getSectorList()
        
    def getIndustryList (self):
        industryVolatility = dict()
        industryRisk = dict()
        industryReturn = dict()
    

        # read csv file and create dictionary for each column
        with open('Back-End/industry_performance.csv') as csvfile:
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

        
        
        p1 = SelectionByPerformance(self.holdingPeriod, self.riskLevel, industryVolatility, industryRisk, industryReturn)
        industryList = p1.getPerformanceList() 
        return industryList
    
        

