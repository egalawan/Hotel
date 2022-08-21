import pandas as pd
import csv
class Manager():
    def show_report(self):
        print("yo")
        with open('user_data.csv', 'r') as f:
            self.reader2 = csv.reader(f)
            #next(self.reader2)
            for row in self.reader2:
                data = " ".join(row)
            return data 

        ##we can have multiple managers with different passwords if we need?

    def manager():
        manager = "joe"
        print(manager)
