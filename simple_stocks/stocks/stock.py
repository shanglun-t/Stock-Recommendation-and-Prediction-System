import csv
from .industry import *
from decimal import *


def getStockInfo(industryList):
    ticker = list()

    with open('Back-End/industry_performance.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)

        result = list()

        for row in reader:
            if row[2] in industryList:
                data = (row[0], row[1], row[2],Decimal(float(row[5])*100).quantize(Decimal('1.00')))
                result.append (data)
    return result

class StockSelection:

    def __init__(self, holdingPeriod, riskLevel):
        self.holdingPeriod = holdingPeriod
        self.riskLevel = riskLevel

    def getSelectedStockList(self):
        
        self.industryObj = IndustrySelection(self.holdingPeriod, self.riskLevel)
        self.industryList= self.industryObj.getIndustryList()


        

        return getStockInfo(self.industryList)


st1 = StockSelection('T5', 'R3')
st1.getSelectedStockList()


