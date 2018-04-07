import csv
from .stock import *
from operator import itemgetter
import numpy as np
import os


class StockPrediction:

    def __init__(self, selectedStockList):
        self.selectedStockList = selectedStockList

    def getStockPrediction(self):

        result = list()

        for ticker in self.selectedStockList:

            # gets current price from historical data csv files
            root1 = 'Back-End/historical_data'
            extention = str('.csv')
            file1 = ticker[0] + extention
            currentPrice = None

            with open(os.path.join(root1, file1)) as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                next(reader)
                for row in reader:
                    try:
                        currentPrice =  float(row[5])
                    except:
                        pass

            root = 'Back-End/pred_results'
            extention = str('_res.csv')
            file = ticker[0] + extention
            dailyPredictionPrice = np.array([])
            with open (os.path.join(root, file)) as csvfile:
                reader = csv.reader(csvfile, delimiter=',')


                next(reader)

                for row in reader:
                    try:
                        dailyPredictionPrice = np.append(dailyPredictionPrice, (float(row[0])))
                    except:
                        pass
            PredictedPrice = np.mean(dailyPredictionPrice)
            growthRate = ((PredictedPrice-currentPrice) / currentPrice) * 100
            data = (ticker[0], ticker[1], ticker[2], ticker[3],Decimal(ticker[4]).quantize(Decimal('1.00')),
                    Decimal(currentPrice).quantize(Decimal('1.00')),Decimal(PredictedPrice).quantize(Decimal('1.00')),
                    Decimal(growthRate).quantize(Decimal('1.00')))
            result.append (data)

        sortedResult = sorted(result, key=itemgetter(7), reverse=True)

        return sortedResult

