import random
import time
import core.utils as utils

class TrainingUnit:
    
    def __init__(self, utype = -1):
        if utype == -1:
            self.unitType = random.randint(0, 3)
        else:
            self.unitType = utype

        self.firstInt = 0
        self.secondInt = 0
        self.result = 0
        self.time = 0
        self.generateNumbers()

    def enterAnswer(self):
        ans = 0
        startTime = time.time()
        while ans != self.result:
            utils.clear()
            self.showUnit()
            try:
                ans = int(input())
            except ValueError:
                ans = 0

        return (time.time() - startTime)

    def generateNumbers(self):
        if self.unitType == 1:
            self.secondInt = random.randint(1, 99)
            self.result = random.randint(1, 99)
            self.firstInt = self.secondInt + self.result
        elif self.unitType == 3:
            self.secondInt = random.randint(1, 33)
            self.result = random.randint(1, 33)
            self.firstInt = self.secondInt * self.result
        else:
            self.firstInt = random.randint(1, 99)
            self.secondInt = random.randint(1, 99)
            if self.unitType == 0:
                self.result = self.firstInt + self.secondInt
            elif self.unitType == 2:
                self.result = self.firstInt * self.secondInt

    def setUnitTime(self, time):
        self.time = time
    
    def getUnitTime(self):
        return self.time
    
    def getUnitData(self):
        return (self.firstInt, self.secondInt, self.unitType, self.result)