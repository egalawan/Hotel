import tkinter as tk
#from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import csv
from csv import *
import pandas as pd
from tkinter import messagebox
from tkinter.messagebox import showinfo
from database import  Database
from customer import Customer

import csv
import pandas as pd


class HotelGUI():
    """
    Date: August 02, 2022

    Programmer:Thisura Nawalage

    A hotel experience is simulated with a GUI.

    A hotel GUI is shown. This hotel class that holds all of our methods. 
    This class simulates the functionality of a hotel with all of our included methods. 

    Methods list:
    FrontPage
    OpenRooms
    GoBack
    ConfirmPage
    OpenModify
    AddLastName
    LastNameConf

    Parameters:
    None

    Returns:
    None
    """

    #--------------------------------------------------------------------------------------------------#
    def __init__(self):
        """
        Date:August 02, 2022

        Programmer:Thisura Nawalage

        This is the main GUI window for the user to interact with.

        Creates the 'interface' and we can change the title of the window and can also the dimensions of the window, and the color
        We also create multiple frames that are used to be pages on the interface. 

        Parameters:
        None

        Returns:
        None
        """

        self.window = tk.Tk()
        self.window.title("Hotel Scrummy")
        #self.window.configure(bg = '#458B74')
        self.window.geometry('420x420')

        #Creating each 'window' space for the information
        self.main = tk.Frame(self.window)
        self.confirm = tk.Frame(self.window)
        self.RegisterNewUser = tk.Frame(self.window)
        self.ViewAvailableRooms = tk.Frame(self.window)
        self.ModifyReservation = tk.Frame(self.window)

        #calling the main page and the labels and buttons assigned to 'main'
        
        self.FrontPage()
        self.window.mainloop()
        ##end Main Window
    #--------------------------------------------------------------------------------------------------#
    #Behaviors -Methods

    #--------------------------------------------------------------------------------------------------#
    #Main Page
    def FrontPage(self):
     
        """
        Date:August 02 2022

        Programmer:Arturo Zenteno/Thisura Nawalage

        Displays the front page.

        Displays the front page and all of the functional buttons that are on it along with a photo of our hotel.

        Parameters:
        None

        Returns:
        None
        """
        #Labels for main Window
        #Main Window Start
        self.main.pack(side = TOP)

        #self.canvas_ = Canvas(self.main, width=250, height=250)
        

        self.welcome_text = tk.Label(self.main, text ="Welcome to Hotel Scrummy",
                                                font = ("Georgia", 20), fg= "#578ee6")

        self.Info_text = tk.Label(self.main, text ="from Team Damp",
                                                font = ("Times New Roman", 15), fg= "#ffb3e9")
                                                

        # self.buttonLogin = tk.Button(self.main, text = 'Log In',
        #                                               activebackground = 'green',
        #                                               foreground= "green",
        #                                               command = self.OpenLogin)

        # self.buttonRegister = tk.Button(self.main, text = 'Register', 
        #                                 command = self.OpenRegister)
        
        self.buttonOpenRooms = tk.Button(self.main, text = 'Available rooms', 
                                        command = self.OpenRooms)

        self.buttonModify = tk.Button(self.main, text = 'Cancel reservation', 
                                        command = self.OpenModify)
        
        #image
        #self.image_file = Image.open("backgroudphoto.png")
        #resize the image
        #self.resize_image = self.image_file.resize((150,150))

        self.pic_ = Image.open("hotel.webp")
        self.pic_resize = self.pic_.resize((150,150))
        self.my_img = ImageTk.PhotoImage(self.pic_resize)

        #making the label
        self.labelImage = tk.Label(self.main,image=self.my_img)
        #self.labelImage.image = self.my_img
        
        #quit button
        button_quit = tk.Button(self.main, text = 'Exit', 
                                                command = self.window.destroy)
        

        #Main Window Page with all the functions to show the order on the page
        #.pack and .pack() are like the printing on the gui,
        #there are different ways to print .pack makes it a little easier to place
        #the buttons and labels next to each other
        
        self.labelImage.pack(pady=5)

        #self.canvas_.pack(row = 5, column = 1)
        self.welcome_text.pack()
        self.Info_text.pack(pady= 10)

        #buttons on main window in order
        # self.buttonLogin.pack(side = LEFT, expand=True, fill = 'x')
        # self.buttonRegister.pack(side = TOP, expand=True, fill = 'x')
        self.buttonOpenRooms.pack(side = TOP, expand=True)
        self.buttonModify.pack(side = TOP, expand=True)
        button_quit.pack(side = BOTTOM, expand=True)
        

    #--------------------------------------------------------------------------------------------------#

    #--------------------------------------------------------------------------------------------------#
    def Go_back(self):
        """Returns to the front page"""
        #'forgetting each of the last pages
        self.RegisterNewUser.pack_forget()
        self.ViewAvailableRooms.pack_forget()
        self.ModifyReservation.pack_forget()
        #adding the main page

        self.main.pack()


    #'''showing the users all the rooms that are open "inventory"
    #--------------------------------------------------------------------------------------------------#
    def OpenRooms(self):
        """
        Date:August 4, 2022

        Programmer:Phone Pyae Zaw/Mithell Berbera

        Displays available rooms.

        Displays all of the rooms within our hotel and allows for user selection.

        Parameters:
        None

        Returns:
        None
        """
        self.ModifyReservation.pack_forget()
        self.main.pack_forget()
        self.ViewAvailableRooms.pack()
        
        self.availableRooms = tk.Label(self.ViewAvailableRooms, text ="Book a Room",
                                                font = ("Georgia", 20), fg="#578ee6")
        self.availableRooms.pack(side= TOP, pady= 10)
        
        with open('hotels.csv', 'r') as f:
            reader = csv.reader(f)
            #skips first line
            next(reader)
            ## WORK ON THIS PART
            for row in reader:
                self.information = tk.Label(self.ViewAvailableRooms, text=" ".join(row))
                self.information.pack() 

                ##dont think this part does anything 
        #####################################
        self.select_Room = tk.Label(self.ViewAvailableRooms, text ="Select Room:")
        self.room_entry = Entry(self.ViewAvailableRooms)
        
        self.name = tk.Label(self.ViewAvailableRooms, text ="What is your name:")
        self.name_entry = Entry(self.ViewAvailableRooms)
        
        self.email = tk.Label(self.ViewAvailableRooms, text ="What is your email:")
        self.email_entry = Entry(self.ViewAvailableRooms)
        
        self.room_button = tk.Button(self.ViewAvailableRooms, text = "Confirm Room", 
                                                                command = self.confirm_Page)
        
        self.select_Room.pack(pady=4)
        self.room_entry.pack(pady= 1)
        self.name.pack(pady=4)
        self.name_entry.pack(pady= 1)

        self.email.pack(pady=4)
        self.email_entry.pack(pady= 1)

        
        self.room_button.pack(side=BOTTOM,pady= 0)
                
        ##need to print out the text file with database

    #--------------------------------------------------------------------------------------------------#
    def confirm_Page(self):
        """
        Date:August 14, 2022

        Programmer:Thisura Nawalage/Arturo Zenteno

        Confirms your room.

        Confirms the user's selected room and marks it as unavailable.

        Parameters:
        None

        Returns:
        None
        """
        #forgetting the previous 'page' and opening up a new page so that the user can see which room they selected 
        #and the information about the room and their stay?
        
        #Database for hotel, writing into file
        room_num = self.room_entry.get()
        Database.book_room(self,room_num)

        #sends user information to another class 
        lst = [self.email_entry.get(), self.room_entry.get(), self.name_entry.get()]
        s = ",".join(lst)
        Database.write_booking(self,s)

        ##
        self.ViewAvailableRooms.pack_forget()

        self.confirm.pack()
        ##TITLE LABEL AGAIN
        
        self.thankyou = tk.Label(self.confirm, text ="Thank you for booking",
                                                font = ("Georgia", 20), fg="#578ee6")
        
        self.pic2_ = Image.open("thankyou.png")
        self.pic2_resize = self.pic2_.resize((350,350))
        self.my_img2 = ImageTk.PhotoImage(self.pic2_resize)

        #making the label
        self.labelImage2 = tk.Label(self.confirm,image=self.my_img2)
        #self.labelImage.image = self.my_img
        self.thankyou.pack(pady= 10)
        self.labelImage2.pack()


    #--------------------------------------------------------------------------------------------------#

    #check user's reservation information, so will need to check the  user database for their information 
    #then check hotel database to see if confirmation number matches a room 

    #--------------------------------------------------------------------------------------------------#
    conf_list = []

    def LastNameConf(self):
        """
        Date:August 8, 2022

        Programmer:Phone Pyae Zaw/Mithell Berbera

        Checks if last name is in the database from the entry from addLastname Method

        This method will check if the last name is in the database and will print out an error if it is non-existent.
        Parameters:
        None

        Returns:
        None
        """
        self.name_Conf=[self.email_entry.get(),
                    self.ConfNum_entry.get()]
        self.conf_list.append(self.name_Conf)

        self.email_conf = self.email_entry.get()
        self.num_conf = self.ConfNum_entry.get()
       
        #self.df = pd.read_csv("hotels.csv")
        #self.df.loc[self.df['Room Number'] == '#' + room, 'Status'] = 'Available'
        #self.df.to_csv("hotels.csv", index = False)

        with open('user_data.csv', 'r') as f:
            self.reader = f.read()
            if self.email_conf in self.reader:
                Database.cancel_room(self,self.num_conf)
                #Customer.name(self)
            else:
                self.ConfNum = tk.Label(self.ModifyReservation, text = 'Error')
                self.ConfNum.pack()
                #self.ModifyReservation.pack_forget()

    def OpenModify(self):
        """
        Date:August 8, 2022

        Programmer:Phone Pyae Zaw/Mithell Berbera

        Modifies user's booking.

        This method will ask for the user's information and allow them to cancel their booking.

        Parameters:
        None

        Returns:
        None
        """
        self.main.pack_forget()
        self.ModifyReservation.pack()

        self.email = tk.Label(self.ModifyReservation, text = 'Enter Email:')
        self.email_entry = Entry(self.ModifyReservation)

        self.ConfNum = tk.Label(self.ModifyReservation, text = 'Enter Room Number:')
        self.ConfNum_entry = Entry(self.ModifyReservation, show = "*")

        self.button_newnext = tk.Button(self.ModifyReservation, text = 'next',
                                        command = self.LastNameConf)

        #back buton duh
        self.back_button = tk.Button(self.ModifyReservation, text = 'back',
                                        command = self.Go_back)

        ### in the window
        self.email.pack()
        self.email_entry.pack()

        self.ConfNum.pack()
        self.ConfNum_entry.pack()
 
        self.button_newnext.pack()
        #printing back button
        self.back_button.pack()
        #On the window
    #--------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    """Calls the main class."""
    base = HotelGUI()
