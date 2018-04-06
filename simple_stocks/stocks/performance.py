import csv
import sys
from collections import OrderedDict
import numpy as np
import scipy as sp
import itertools


class SelectionByPerformance:

    def __init__(self, holdingPeriod, riskLevel, volatility, risk, returns):
        self.holdingPeriod = holdingPeriod
        self.riskLevel = riskLevel
        self.volatility = volatility
        self.risk = risk
        self.returns = returns

    # returns list of Sector with value in range of self.high and self.low
    def reduceByValue(self, low, high, myDict):
        self.result = list()
        for k, v in myDict.items():
            if float(v) >= self.low and float(v) <= self.high:
                self.result.append(k)

        if len(self.result) <= 0:
            self.low = self.low - self.low * 0.3
            if len(self.result) <= 1:
                self.low = self.low - self.low * 0.35
            self.result = []

            self.high = self.high + self.high * 0.3

            for k, v in myDict.items():
                if float(v) >= self.low and float(v) <= self.high:
                    self.result.append(k)

        return self.result

    # provides list of Sector based on volatility and risk chosen by the user
    def getPerformanceList(self):

        # create 5 groups of sector based on volatility
        self.low = min(float(self.volatility[k]) for k in self.volatility)
        self.high = max(float(self.volatility[k]) for k in self.volatility)

        self.diff = (self.high - self.low) / 5

        # select range of volatility based on user input
        if self.holdingPeriod == 'T1':
            self.low = self.low + self.diff * 4
        if self.holdingPeriod == 'T2':
            self.low = self.low + self.diff * 3
        if self.holdingPeriod == 'T3':
            self.low = self.low + self.diff * 2
        if self.holdingPeriod == 'T4':
            self.low = self.low + self.diff
        if self.holdingPeriod == 'T5':
            pass

        self.high = self.low + self.diff
        # print (' volatility high low',self.high, self.low)

        # reduce the list of sector based on the volatility range
        self.result = self.reduceByValue(self.low, self.high, self.volatility)
        print('Volatility', self.result)

        self.risk = {k: self.risk[k] for k in self.result if k in self.risk}

        # create 2 groups of sector based on risk

        self.low = min(float(self.risk[k]) for k in self.risk)
        self.high = max(float(self.risk[k]) for k in self.risk)

        self.diff = (self.high - self.low) / 2

        # select range of risk based on user input
        if self.riskLevel == 'R1' or self.riskLevel == 'R2':
            self.low = self.low + self.diff
        if self.riskLevel == 'R3' or self.riskLevel == 'R4':
            pass

        self.high = self.low + self.diff
        # print(' risk high low', self.high, self.low)
        # reduce the list of sector based on the risk range
        self.result = self.reduceByValue(self.low, self.high, self.risk)

        print('RISK', self.result)

        self.returns = {k: self.returns[k] for k in self.result if k in self.returns}

        # create 2 groups of sector based on return

        self.low = min(float(self.returns[k]) for k in self.returns)
        self.high = max(float(self.returns[k]) for k in self.returns)
        self.diff = (self.high - self.low) / 2

        # select range of risk based on user input
        self.high = self.low + self.diff

        # reduce the list of sector with self.highest return
        self.result = list()
        for k, v in self.returns.items():
            if float(v) >= self.high:
                self.result.append(k)

        return self.result

        
        
