import pygame
import gui.elements as elements
import core.training_session as session

class SessionScreen:

    def __init__(self, size, callbacks):
        self.currentUnit = -1
        self.trainingSession = session.TrainingSession()

        self.background = (245, 245, 245)
        self.elements = [
            elements.Text("420", (size[0] / 2 + 60, 150), 50, 2),
            elements.Text("5356", (size[0] / 2 + 60, 190), 50, 2),
            elements.Text("+", (size[0] / 2 - 60, 190), 50, 0),
            elements.Rectangle((size[0] / 2, 230), (150, 2)),
            elements.Text("5776", (size[0] / 2 + 60, 240), 50, 2),
            elements.Text(str(self.currentUnit + 1) + "/10", (size[0] / 2, size[1] - 50), 20, 0),
            elements.Button("Suivant", (size[0] / 2, size[1] - 150), (200, 50), self.updateCurrentUnit),
        ]

        self.updateCurrentUnit()

    def updateCurrentUnit(self):
        if self.currentUnit < 9:
            self.currentUnit += 1 
            data = self.trainingSession.getUnits()[self.currentUnit].getUnitData()
            self.elements[0].changeText(str(data[0]))
            self.elements[1].changeText(str(data[1]))
            self.elements[4].changeText(str(data[3]))
            self.elements[5].changeText(str(self.currentUnit + 1) + "/10")

            if data[2] == 0:
                self.elements[2].changeText("+")
            elif data[2] == 1:
                self.elements[2].changeText("-")
            elif data[2] == 2:
                self.elements[2].changeText("x")
            elif data[2] == 3:
                self.elements[2].changeText("÷")

    def handleEvent(self, event):
        for e in self.elements:
            e.handleEvent(event)

    def display(self, screen, size):
        screen.fill(self.background)

        for e in self.elements:
            screen.blit(e.getElement(), e.getRect())

        return screen