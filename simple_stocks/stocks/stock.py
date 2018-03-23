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

        for row in reader:
            #print (row[3])
            if str(row[3]) in industryList:
                print('\nthis is user indus\n', industryList)
                data = (row[0], row[1], row[2], row [3], Decimal(float(row[6])*100).quantize(Decimal('1.00')))
                result.append (data)
            else:
                result = ['nothing added', 'lol']
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

        self.indusrtyListByUser = list ()
        for elm in indusrtyListByUser:
            print (elm)
            self.indusrtyListByUser.append(str(elm))

        return getStockInfo(self.indusrtyListByUser)



