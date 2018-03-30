import csv
<<<<<<< HEAD
from numpy.core.defchararray import strip
=======

from numpy.core.defchararray import strip

>>>>>>> 564850d547b22da8f2fff1a2f2fd569ee6eb5fab
from .industry import *
from decimal import *


def getStockInfo(industryList):
<<<<<<< HEAD
=======
    ticker = list()

>>>>>>> 564850d547b22da8f2fff1a2f2fd569ee6eb5fab

    with open('Back-End/industry_performance.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
<<<<<<< HEAD
        result = list()
        print (industryList)
        for row in reader:
            data = (row[0], row[1], row[2], row[3], Decimal(float(row[6])* 10 * 252 ).quantize(Decimal('1.00')))

            if data[3] in industryList:
                #data = (row[0], row[1], row[2], row[3], Decimal(float(row[6])*100).quantize(Decimal('1.00')))
                result.append (data)
=======

        result = list()

        for row in reader:
            #print (row[3])
            if str(row[3]) in industryList:
                print('\nthis is user indus\n', industryList)
                data = (row[0], row[1], row[2], row [3], Decimal(float(row[6])*100).quantize(Decimal('1.00')))
                result.append (data)
            else:
                result = ['nothing added', 'lol']
>>>>>>> 564850d547b22da8f2fff1a2f2fd569ee6eb5fab
    return result

class StockSelection:

    def __init__(self, holdingPeriod, riskLevel):
        self.holdingPeriod = holdingPeriod
        self.riskLevel = riskLevel

    def getSelectedStockList(self):
<<<<<<< HEAD
        self.industryObj = IndustrySelection(self.holdingPeriod, self.riskLevel)
        self.industryList= self.industryObj.getIndustryList()

=======

        self.industryObj = IndustrySelection(self.holdingPeriod, self.riskLevel)
        self.industryList= self.industryObj.getIndustryList()


>>>>>>> 564850d547b22da8f2fff1a2f2fd569ee6eb5fab
        return getStockInfo(self.industryList)


    def getUserSelectedStockList(self, indusrtyListByUser):

<<<<<<< HEAD
        self.indusrtyListByUser = indusrtyListByUser
        result = list()

        for elm in self.indusrtyListByUser:
            result.append(elm)

        return getStockInfo(self.indusrtyListByUser)



=======
        self.indusrtyListByUser = list ()
        for elm in indusrtyListByUser:
            print (elm)
            self.indusrtyListByUser.append(str(elm))

        return getStockInfo(self.indusrtyListByUser)

>>>>>>> 564850d547b22da8f2fff1a2f2fd569ee6eb5fab
