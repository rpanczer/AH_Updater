import tkinter as tk
import os
import zipfile
import datetime

class Application(tk.Frame):

    filename = "hi"

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        # Instantiate widgets
        self.filePathDisplay = tk.Entry(self)
        self.browseButton = tk.Button(self, text='Browse...', command=createfolder)
        self.runButton = tk.Button(self, text='Run', fg='white', background='green')
        self.quitButton = tk.Button(self, text='Quit', fg='white', background='red', command=self.quit)
        self.createwidgets()

    def createwidgets(self):
        # Arrange widgets on the grid layout
        self.filePathDisplay.grid(row=0, column=0)
        self.browseButton.grid(row=0, column=3)
        self.runButton.grid(row=1, column=0)
        self.quitButton.grid(row=1, column=3)
"""
    def browseFile():
        print(Application.filename)
        foldername = "templates/{}".filename
        global templatepath = "templates_todeploy/{}".format(foldername)
        createFolder()
"""
def createfolder():
    #Make the path for the template folder general at some point
    path = "C:/Users/rpanczer/PyCharmProjects/AH_Updater/templates_archive/template"
    foldercheck = os.path.exists(path)
    if foldercheck == 0:
        os.mkdir(path, 0o755)
        print("trace :: Template folder created")
    else:
        print("trace :: Template folder already exists")
    now = datetime.datetime.now()
    zipsyntax = str(now.day) + "_" + str(now.month) + "_" + str(now.year)
    print(zipsyntax)
    """
    zippath = "{}".format(zipsyntax)
    zipfile.ZipFile(zippath, mode="r", compression= ZIP_STORED, allowZip64= true)
    """