from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class Calx(Widget):
    startSessionBtn = ObjectProperty(None)
    workloadBtn = ObjectProperty(None)
    exitBtn = ObjectProperty(None)

    def startSession(self):
        print("Start session")

    def workload(self):
        print("Workload")

    def exitApp(self):
        print("Exit")

class CalxApp(App):
    def build(self):
        calx = Calx()
        return calx

if __name__ == '__main__':
    CalxApp().run()