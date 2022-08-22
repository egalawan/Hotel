import csv
import pandas as pd

class Database():
    def write_booking(self,room,name,email):
            #sends room, name, and email information to be written into user_data.csv
            with open("user_data.csv","a") as f:
                f.writelines(room + "," + name + ","+ email + "\n")
            return 2

    def book_room(self,room_num,name_,email_):
        #our rooms with the index number
        rooms = {"12":0, "42":1, "11":2, "72":3, "69420":4}
        #panda reading to inventory
        df = pd.read_csv("inventory.csv")
        
        if room_num not in rooms:
                #checking if the room is in the rooms array
                self.nonexist = "This room doesn't exist."
                return 1

        elif (df["Status"].values[rooms[room_num]] == "Unavailable"):
                #checks the inventory to see if the room is already book by another customer
                self.text_taken ="This room is Unavailable."
                return 3

        elif (df["Status"].values[rooms[room_num]] == "Available"):
                #if the room is available then change it to unavailable
                df.loc[df['Room Number'] == '#' + str(room_num), 'Status'] = 'Unavailable'
                df.to_csv("inventory.csv", index=False)
                #return 2 so that it will run the next step which is showing the confirmation page
                return Database.write_booking(self,room_num,name_,email_)
        
    
        
    def num_users(self):
        user_count = 0
        for row in open("user_data.csv"):
            (row)
            user_count+= 1
        #self.df = pd.read_csv("user_data.csv")
        #self.user = len(self.df)
        new = str(user_count)
        return new
    #--------------------------#

    def cancel_room(self,room_num,email):
        self.rooms = {"12":0, "42":1, "11":2, "72":3, "69420":4}
        
        self.df = pd.read_csv("inventory.csv")
        self.user_df2 = pd.read_csv("user_data.csv")
        in_file =self.user_df2.isin([email]).any().any() 

        if (room_num not in self.rooms):
            print("This room doesn't exist.")
            return 0

        elif (self.df["Status"].values[self.rooms[room_num]] == "Available"):
            print("This room is already available. No need to cancel.")
            return 1
        
        ##need to work on cancel room still
        #locate if the room number that the user input and the 
        elif (in_file):
                #deletes the row in user_data.csv that has the email in it
                self.user_df2.drop(self.user_df2[(self.user_df2['Email'] == email)].index, inplace=True)
                self.user_df2.to_csv("user_data.csv", index=False)

                #changing inventory.csv so it says available
                self.df.loc[self.df['Room Number'] == '#' + str(room_num), 'Status'] = 'Available'
                self.df.to_csv("inventory.csv", index=False)

                if (self.df["Status"].values[self.rooms[room_num]] == "Available"):
                    self.df.to_csv("inventory.csv", index=False)
                    print("You have cancelled your booking.")   
                ###delete from the user_data.csv
                return 2
        
        ##
                 
        
        