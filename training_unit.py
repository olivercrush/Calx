import random
import os
import time

class TrainingUnit:
    unitType = -1
    firstInt = 0
    secondInt = 0
    result = 0

    def __init__(self):
        self.unitType = random.randint(0, 3)
        self.generateNumbers()

    def clear(self):
        if (os.name == 'nt'):
            os.system("cls")
        else:
            os.system("clear")

    def enterAnswer(self):
        ans = 0
        startTime = time.time()
        while ans != self.result:
            #self.clear()
            self.showUnit()
            ans = int(input())

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
            elif self.unitType == 1:
                self.result = self.firstInt - self.secondInt
            elif self.unitType == 2:
                self.result = self.firstInt * self.secondInt
    
    def showUnit(self):

        strFirstInt = str(self.firstInt)
        strSecondInt = str(self.secondInt)
        strResult = str(self.result)

        if self.unitType == 0:
            print(strFirstInt + " + " + strSecondInt + " = ")
        elif self.unitType == 1:
            print(strFirstInt + " - " + strSecondInt + " = ")
        elif self.unitType == 2:
            print(strFirstInt + " * " + strSecondInt + " = ")
        elif self.unitType == 3:
            print(strFirstInt + " / " + strSecondInt + " = ")