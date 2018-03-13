import csv 
import sys
from collections import OrderedDict
import numpy as np
import scipy as sp
import os
import stocks.industry
import functools as ft



def getStockInfo(industryList):
    ticker = list()

    with open('/Users/shangluntsai/Capstone/simple_stocks/static/csv/industry_performance.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)

        for row in reader:
            if row[2] in industryList:
                print(row[0], row[1], row[2], row[3], row[4], row[5])
    return 'Done'

class StockSelection:

    def __init__(self, holdingPeriod, riskLevel):
        self.holdingPeriod = holdingPeriod
        self.riskLevel = riskLevel

    def getSelectedStockList(self):
        
        self.industryObj = industry.IndustrySelection(self.holdingPeriod, self.riskLevel)
        self.industryList= self.industryObj.getIndustryList()

        getStockInfo(self.industryList)
        

        return 'lo'


#st1 = StockSelection('T5', 'R3')
#st1.getSelectedStockList()

