import csv
import pandas as pd

class Database():
    def write_booking(self,room,name,email):
            with open("user_data.csv", 'a') as f:
                self.header = ['Room Number,Name,Email']
                self.num_of_users = pd.read_csv("user_data.csv")
                print("Number of user", len(self.num_of_users))
                f.writelines("\n" + room + "," + name + ","+ email)

    def book_room(self,room_num):
        rooms = {"12":0, "42":1, "11":2, "72":3, "69420":4}
        #room_num = "12"
        df = pd.read_csv("inventory.csv")
        
        if room_num not in rooms:
                print("This room doesn't exist.")
                return 0

        elif (df["Status"].values[rooms[room_num]] == "Unavailable"):
                print("This room is Unavailable.")
                return 1

        elif (df["Status"].values[rooms[room_num]] == "Available"):
                df.loc[df['Room Number'] == '#' + str(room_num), 'Status'] = 'Unavailable'
                df.to_csv("inventory.csv", index=False)
                print("Your reservation was made.")
                print(len(df))
                return 2
        
    def show_report(self):
        self.df = pd.read_csv("user_data.csv")
        return self.df.head()
        
    def num_users(self):
        self.df = pd.read_csv("user_data.csv")
        self.user = len(self.df)
        new = str(self.user)
        return new
    
    def cancel_room(self,password,room_num,email):
        self.rooms = {"12":0, "42":1, "11":2, "72":3, "69420":4}
        self.real = {"0":0, "1":1, "2":2, "3":3, "4":4}
        
        self.df = pd.read_csv("inventory.csv")
        self.df2 = pd.read_csv("user_data.csv")

        if (room_num not in self.rooms):
            print("This room doesn't exist.")
            return 0

        elif (self.df["Status"].values[self.rooms[room_num]] == "Available"):
            print("This room is already available. No need to cancel.")
            return 1
        
        #######need to work on cancel room still
        elif (self.df2["Room Number"].values[self.real[password]] == room_num):
            print("hello")
            self.df2.drop(index = password)
            #self.df2.to_csv("room_data.csv", index =False)
            if (self.df.loc[self.df['Room Number'] == '#' + str(room_num), 'Status'] == 'Available'):
                (self.df["Status"].values[self.rooms[room_num]] == "Unavailable")
                self.df.to_csv("inventory.csv", index=False)
                print("You have cancelled your booking.")   
                ###delete from the user_data.csv
            return 2
                 
        
        