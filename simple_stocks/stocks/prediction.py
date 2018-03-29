import csv
from .stock import *
from operator import itemgetter


class StockPrediction:

    def __init__(self, selectedStockList):
        self.selectedStockList = selectedStockList

    def getStockPrediction(self):
        result = self.selectedStockList
        ''''
        for stock in self.selectedStockList:
            file = 'Back-End/historical_data/' + stock + '.csv'
            print('this is file name', file)
            with open (file) as csvfile:

                closePrice = None
                predictedPrice = None
                predictedGrowth = None
                reader = csv.reader(csvfile, delimiter=',')
                next(reader)
                for row in reader:
                    try:
                        closePrice = row[5]
                    except:
                        pass
                    #prediction calcultaion here for each stock
                    #growth calculation predictedGrowth = (closePrice - predictedPrice) / 100
            data = (stock[0], stock[1], stock[2], stock[3], stock[4], float(closePrice), predictedPrice, predictedGrowth)
            result.append (data )

        '''
        sortedResult = sorted(result, key=itemgetter(4), reverse=True)

        return sortedResult
