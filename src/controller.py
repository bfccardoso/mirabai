"""
Created on Apr 29, 2020

@author: Bruno Cardoso
"""
import tkinter as tk

from defines import *


class Controller(object):
    def __init__(self):
        """
        Constructor
        """
        self.root = tk.Tk()
        self.root.title(TITLE + VERSION)
        self.root.geometry(SIZE_WINDOW)

    def main(self):
        self.root.mainloop()