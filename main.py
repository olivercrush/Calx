from tkinter import *
import core.training_session as s

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Calx")
        self.pack(fill=BOTH, expand=1)
        quitLabel = Label(self, text="Quitter")
        quitLabel.place(x=0, y=0)

    def exit_window(self):
        exit()

#session = s.TrainingSession()

root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()