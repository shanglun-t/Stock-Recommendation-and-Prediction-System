import csv
from numpy.core.defchararray import strip

from .industry import *
from decimal import *


def getStockInfo(industryList):

    ticker = list()



    with open('Back-End/industry_performance.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)

        result = list()
        print (industryList)
        for row in reader:
            data = (row[0], row[1], row[2], row[3], Decimal(float(row[6])* 10 * 252 ).quantize(Decimal('1.00')))

            if data[3] in industryList:
                #data = (row[0], row[1], row[2], row[3], Decimal(float(row[6])*100).quantize(Decimal('1.00')))
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


    def getUserSelectedStockList(self, indusrtyListByUser):

        self.indusrtyListByUser = indusrtyListByUser
        result = list()

        for elm in self.indusrtyListByUser:
            result.append(elm)

        return getStockInfo(self.indusrtyListByUser)


