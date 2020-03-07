import training_unit as u

class TrainingSession:

    def __init__(self):
        for i in range(0, 10):
            tmp = u.TrainingUnit()
            print(str(tmp.enterAnswer()) + "s")
