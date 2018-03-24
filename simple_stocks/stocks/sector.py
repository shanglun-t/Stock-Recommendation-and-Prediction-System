import csv
from .performance import *


class SectorSelection:

    def __init__(self, holdingPeriod, riskLevel):
        self.holdingPeriod = holdingPeriod
        self.riskLevel = riskLevel
    
    # provides list of Sector based on volatility and risk chosen by the user 
    def getSectorList(self):
        
        sectorVolatility = dict()
        sectorRisk = dict()
        sectorReturn = dict()
        
        
        # read csv file and create dictionary for each column
        with open('Back-End/sector_performance.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)

            for row in reader:
                sectorVolatility[row[0]] = row[1]
                sectorRisk[row[0]] = row[2]
                sectorReturn[row[0]] = row[3]

        s1 = SelectionByPerformance(self.holdingPeriod, self.riskLevel, sectorVolatility, sectorRisk, sectorReturn)
        sectorList = s1.getPerformanceList() 
        #print ('Selected Sector List', s1.getPerformanceList())
        return sectorList       






