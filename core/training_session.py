import core.training_unit as u
import core.utils

class TrainingSession:
    def __init__(self):
        self.units = []
        self.sessionWorkload = 0

        for i in range(0, 10):
            self.units.append(u.TrainingUnit())

    def getUnits(self):
        return self.units

    def getAverageTime(self):
        unitSum = 0
        for u in self.units:
            unitSum += u.getUnitTime()

        return round(unitSum / len(self.units), 2)
