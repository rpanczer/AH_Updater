import tkinter as tk
from tkinter import filedialog as fd
import os


class Application(tk.Frame):

    filename = "hi"

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        # Instantiate widgets
        self.filePathDisplay = tk.Entry(self)
        self.browseButton = tk.Button(self, text='Browse...', command=browseFile)
        self.runButton = tk.Button(self, text='Run', fg='white',background='green')
        self.quitButton = tk.Button(self, text='Quit', fg='white', background='red', command=self.quit)
        self.createWidgets()

    def createWidgets(self):
        # Arrange widgets on the grid layout
        self.filePathDisplay.grid(row=0, column=0)
        self.browseButton.grid(row=0, column=3)
        self.runButton.grid(row=1, column=0)
        self.quitButton.grid(row=1, column=3)


def browseFile():
    print(Application.filename)