import pygame
import gui.elements as elements
import core.training_session as session

class SessionScreen:

    def __init__(self, size, callbacks):
        self.currentUnit = -1
        self.callbacks = callbacks
        self.trainingSession = session.TrainingSession()
        self.userAnswer = ""

        self.background = (245, 245, 245)
        self.elements = [
            elements.Text("420", (size[0] / 2 + 60, 150), 50, 2),
            elements.Text("5356", (size[0] / 2 + 60, 190), 50, 2),
            elements.Text("+", (size[0] / 2 - 60, 190), 50, 0),
            elements.Rectangle((size[0] / 2, 230), (150, 2)),
            elements.Text("", (size[0] / 2 + 60, 240), 50, 2),
            elements.Text(str(self.currentUnit + 1) + "/10", (size[0] / 2, size[1] - 50), 20, 1),
            #elements.Button("Suivant", (size[0] / 2, size[1] - 150), (200, 50), self.updateCurrentUnit),
        ]

        self.updateCurrentUnit()

    def checkAnswer(self):
        data = self.trainingSession.getUnits()[self.currentUnit].getUnitData()
        if data[3] == int(self.userAnswer):
            self.updateCurrentUnit()

    def updateCurrentUnit(self):
        self.userAnswer = ""
        if self.currentUnit < 9:
            self.currentUnit += 1 
            data = self.trainingSession.getUnits()[self.currentUnit].getUnitData()
            self.elements[0].changeText(str(data[0]))
            self.elements[1].changeText(str(data[1]))
            self.elements[4].changeText(self.userAnswer)
            self.elements[5].changeText(str(self.currentUnit + 1) + "/10")

            if data[2] == 0:
                self.elements[2].changeText("+")
            elif data[2] == 1:
                self.elements[2].changeText("-")
            elif data[2] == 2:
                self.elements[2].changeText("x")
            elif data[2] == 3:
                self.elements[2].changeText("÷")
        else:
            self.callbacks[4](5)

    def handleEvent(self, event):
        self.checkUserInput(event)
        for e in self.elements:
            e.handleEvent(event)

    def checkUserInput(self, event):
        if event.type == pygame.KEYDOWN:
            try:
                key = int(pygame.key.name(event.key))

                if not (len(self.userAnswer) == 0 and key == 0):
                    self.userAnswer = self.userAnswer + str(key)
                    self.elements[4].changeText(str(self.userAnswer))
                    self.checkAnswer()
            except ValueError:
                if pygame.key.name(event.key) == "backspace":
                    self.userAnswer = self.userAnswer[:-1]
                    self.elements[4].changeText(str(self.userAnswer))



    def display(self, screen, size):
        screen.fill(self.background)

        for e in self.elements:
            screen.blit(e.getElement(), e.getRect())

        return screen