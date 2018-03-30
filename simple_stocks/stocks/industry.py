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
                #print (row [0], row [1], row[2], row[3], row[4], row[5],row[6])
                if str(row[2]) in self.selectedSectorList:
                    industryVolatility.setdefault(row[3], []).append(float(row[4]))
                    industryRisk.setdefault(row[3], []).append(float(row[5]))
                    industryReturn.setdefault(row[3], []).append(float(row[6]))



        for k, v in industryVolatility.items():
            industryVolatility[k] = ft.reduce(lambda x, y: x + y, v) / len(v)
        for k, v in industryRisk.items():
            industryRisk [k] = ft.reduce(lambda x, y: x + y, v) / len(v)
        for k, v in industryReturn.items():
            industryReturn [k] = ft.reduce(lambda x, y: x + y, v) / len(v)

        
        
        p1 = SelectionByPerformance(self.holdingPeriod, self.riskLevel, industryVolatility, industryRisk, industryReturn)
        industryList = p1.getPerformanceList() 
        return industryList
<<<<<<< HEAD
    
        

=======
>>>>>>> 564850d547b22da8f2fff1a2f2fd569ee6eb5fab
