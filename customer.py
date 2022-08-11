import tkinter
import csv
from tkinter import Tk

class Customer():
    def name(self):
        file = open('hotels.csv', 'r')
        with file:
            self.reader = csv.reader(file)
            for row in self.reader:
                print(row)
                for e in row:
                    self.information = tkinter.Label(self.window, text = row)
                self.information.pack()
            
d = Customer()