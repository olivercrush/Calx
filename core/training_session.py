import training_unit as u
import utils

class TrainingSession:

    unitTimes = []
    sessionWorkload = 0

    def __init__(self):
        for i in range(0, 10):
            tmp = u.TrainingUnit(0)
            self.unitTimes.append(tmp.enterAnswer())

        utils.clear()
        for x in self.unitTimes:
            self.sessionWorkload += x
        self.sessionWorkload /= len(self.unitTimes)
        print("Session workload : " + str(self.sessionWorkload) + "s")
