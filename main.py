import tkinter as tk
#from tkinter import ttk
from tkinter import *
from turtle import left
from PIL import Image, ImageTk
import csv
from csv import *
import pandas as pd
from tkinter import messagebox
from tkinter.messagebox import showinfo
from database import Database
from manager import Manager
from receipt import Receipt


class HotelGUI():
    """
    Date: August 02, 2022

    Programmer:Thisura Nawalage

    A hotel experience is simulated with a GUI.

    A hotel GUI is shown. This hotel class that holds all of our methods. 
    This class simulates the functionality of a hotel with all of our included methods. 

    Methods list:
    FrontPage
    GoBack
    OpenRooms
    ConfirmPage
    OpenManagerPage
    ManagerPage
    GoHome
    CancelBooking
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
        self.window.geometry('600x600')

        #Creating each 'window' space for the information to print onto
        self.main = tk.Frame(self.window)
        self.view_rooms = tk.Frame(self.window)
        self.manager_page = tk.Frame(self.window)
        self.manager_bottom = tk.Frame(self.window)
        self.cancel_reservation = tk.Frame(self.window)
        self.confirm = tk.Frame(self.window) #after booking frame to show photo and thanks user for booking with us
        
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

        self.main.pack()

        #self.canvas_ = Canvas(self.main, width=250, height=250)
        
        ##each of the different 'words' on the gui page welcoming the user
        self.welcome_text = tk.Label(self.main, text ="Welcome to Hotel Scrummy",
                                                font = ("Georgia", 25), fg= "#578ee6")

        self.Info_text = tk.Label(self.main, text ="from Team Damp",
                                                font = ("Georgia", 15), fg= "#ffb3e9")
                                                
        ## Four buttons that we show up on the front page of the GUI

        self.buttonOpenRooms = tk.Button(self.main, text = 'Available rooms', 
                                        command = self.OpenRooms)
        
        self.buttonManager = tk.Button(self.main, text = 'Manager', 
                                        command = self.OpenManagerPage)

        self.buttonModify = tk.Button(self.main, text = 'Cancel reservation', 
                                        command = self.CancelBooking)
        
        #quit button
        button_quit = tk.Button(self.main, text = 'Exit', 
                                                command = self.window.destroy)

        #image
        #self.image_file = Image.open("backgroudphoto.png")
        #resize the image
        #self.resize_image = self.image_file.resize((150,150))

        self.pic_ = Image.open("hotel.webp")
        self.pic_resize = self.pic_.resize((250,250))
        self.my_img = ImageTk.PhotoImage(self.pic_resize)

        #making the label
        self.labelImage = tk.Label(self.main,image=self.my_img)
        #self.labelImage.image = self.my_img
        
        
        #Main Window Page with all the functions to show the order on the page
        #.pack and .pack() are like the printing on the gui,
        #there are different ways to print .pack makes it a little easier to place
        #the buttons and labels next to each other
        
        self.labelImage.pack(side = TOP, ipadx = 10, ipady = 10, fill = 'both', expand = True)

        #self.canvas_.pack(row = 5, column = 1)
        self.welcome_text.pack(side = TOP)
        self.Info_text.pack(side = TOP, pady= 10)

        #buttons on main window in order
        # self.buttonLogin.pack(side = LEFT, expand=True, fill = 'x')
        # self.buttonRegister.pack(side = TOP, expand=True, fill = 'x')
        self.buttonOpenRooms.pack(side = TOP)
        self.buttonManager.pack(side = TOP)
        self.buttonModify.pack(side = TOP)
        button_quit.pack(side = BOTTOM)
        
    #--------------------------------------------------------------------------------------------------#
    def Go_back(self):
        """Returns to the front page"""
        #'forgetting each of the last pages
        self.view_rooms.pack_forget()
        self.manager_page.pack_forget()
        self.manager_bottom.pack_forget()
        self.confirm.pack_forget()

        #goes back to the main page
        self.main.pack()
    #'''showing the users all the rooms that are open "inventory"
    #--------------------------------------------------------------------------------------------------#

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
        #deletes the previous page
        self.cancel_reservation.pack_forget()
        self.main.pack_forget()
        #shows the widgets that are on the 'view_rooms' page
        self.view_rooms.pack(anchor = "n")
        
        self.availableRooms = tk.Label(self.view_rooms, text ="Book a Room",
                                                font = ("Georgia", 25), fg="#578ee6")
        

        #prints out the title and an extra space
        self.availableRooms.pack(side= TOP, pady= 15)
        
        #reading the inventory.csv to see what rooms are open
        with open('inventory.csv', 'r') as f:
            reader = csv.reader(f)
            #skips first line
            next(reader)
            ## then prints each line onto the book room page
            for row in reader:
                self.information = tk.Label(self.view_rooms, text=" ".join(row))
                self.information.pack(anchor = "nw") 

        #used with open so we dont need to close
        #each label on the window
        self.select_Room = tk.Label(self.view_rooms, text ="Select Room:")
        self.room_entry = Entry(self.view_rooms)
        
        self.name = tk.Label(self.view_rooms, text ="What is your name:")
        self.name_entry = Entry(self.view_rooms)
        
        self.email = tk.Label(self.view_rooms, text ="What is your email:")
        self.email_entry = Entry(self.view_rooms)

        
        self.room_button = tk.Button(self.view_rooms, text = "Confirm Room", 
                                                                command = self.ConfirmPage)
        
        #back buton duh
        self.home_button = tk.Button(self.view_rooms, text = 'Home',
                                        command = self.Go_back)

        #prints out each of the text boxes and entries and buttons after the room info is printed
        self.select_Room.pack(pady=4,side = TOP, anchor= "w")
        self.room_entry.pack(pady= 1,side = TOP, anchor = "w")
        
        self.name.pack(pady=4,side = TOP, anchor = "w")
        self.name_entry.pack(pady= 1,side = TOP, anchor = "w")

        self.email.pack(pady=4,side = TOP, anchor = "w")
        self.email_entry.pack(pady= 1,side = TOP, anchor = "w")

        self.room_button.pack(pady= 0,side = LEFT, anchor = "c")
        self.home_button.pack(side = LEFT)
        
        ##need to print out the text file with database
    #--------------------------------------------------------------------------------------------------#
    
    def ConfirmPage(self):
        """
        Date:August 14, 2022

        Programmer:Thisura Nawalage/Arturo Zenteno

        Page that tells the user that the room they wanted was book and they 
        can come stay at the hotel

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
        name_ = self.name_entry.get()
        
        email_ = self.email_entry.get()
        self.data = Database.book_room(self,room_num,name_,email_)
        
        if(self.data == 1):
            self.no_room = tk.Label(self.view_rooms, text ="This room doesn't exist.")
            self.no_room.pack()
        
        if(self.data == 3):
            self.no_book = tk.Label(self.view_rooms, text ="This room is Unavailable.")
            self.no_book.pack()
            
    
        if (self.data == 2):
            #sends user information to another class 
            self.view_rooms.pack_forget()
            self.confirm.pack() #frame pack

            Receipt.send_email(self,room_num,email_,name_)

            ##TITLE LABEL AGAIN
            self.thankyou_label = tk.Label(self.confirm, text ="Thank you for booking",
                                                    font = ("Georgia", 25), fg="#578ee6")

            self.thankyou_home_button = tk.Button(self.confirm, text = 'Home',
                                        command = self.Go_back)
            
            #changing the size of the picture
            self.pic2_ = Image.open("thankyou.png")
            self.pic2_resize = self.pic2_.resize((350,350))
            self.my_img2 = ImageTk.PhotoImage(self.pic2_resize)

            #making the label
            self.labelImage2 = tk.Label(self.confirm,image=self.my_img2)
            self.thankyou_label.pack(pady= 10)
            self.labelImage2.pack()
            self.thankyou_home_button.pack()
            
        else:
            print("try again")


    #check user's reservation information, so will need to check the  user database for their information 



    #--------------------------------------------------------------------------------------------------#
    def OpenManagerPage(self):
            """
            Date:August 20, 2022

            Programmer:Thisura Nawalage

            The page that allows the 'Manager' of the hotel to see the booked rooms

            Asks the manager for the password to open page

            Parameters:
            None

            Returns:
            None
            """
            self.main.pack_forget()
            #self.manager_page.pack_forget()
            #self.manager_bottom.pack_forget()
            self.manager_page.pack(side = TOP)
            

            #title and layout for the manager page
            self.main_title = tk.Label(self.manager_page, text = "Manager", 
                                                        font = ("Georgia", 25), fg= "#578ee6")
            ##need to ask 'Manager' for password to see which manager they are
            self.manager_pass =tk.Label(self.manager_page, text = "Please enter your password:")
            self.manager_pass_entry = tk.Entry(self.manager_page,show = "*")

            self.manager_pass_button = tk.Button(self.manager_page, text = 'next', 
                                        command = self.ManagerPage)

            #back buton duh
            self.manager_home_button = tk.Button(self.manager_page, text = 'Home',
                                        command = self.Go_home)
            
            self.main_title.pack()

            self.manager_pass.pack()
            self.manager_pass_entry.pack()
            
            self.manager_pass_button.pack()
            self.manager_home_button.pack()
            
            

    def ManagerPage(self):
        """
        Date:August 20 2022

        Programmer:Thisura Nawalage

        Displays the front page.

        Displays the front page and all of the functional buttons that are on it along with a photo of our hotel.

        Parameters:
        None

        Returns:
        None
        """
        password_ = self.manager_pass_entry.get()
            
        self.manager = Manager.manager(self,password_) #returns the Data from the text file to 'data'
        self.data = Manager.show_report(self)
        self.df = pd.read_csv("user_data.csv")

        if self.manager == "no password":
            self.wrong_pass = tk.Label(self.manager_page, text = "Wrong Password")
            self.wrong_pass.pack()
        else:
            self.manager_bottom.pack(side = BOTTOM, fill = BOTH, expand = True)
            self.manager_page.pack_forget()
            self.main_title = tk.Label(self.manager_bottom, text = "Rooms Booked", 
                                                            font = ("Georgia", 25), fg= "#578ee6")
            self.managername = tk.Label(self.manager_bottom,text = "Welcome Manager: " + (self.manager), 
                                                            font = ("Georgia", 15))

            self.information = tk.Label(self.manager_bottom, text = (self.data), 
                                                            font = ("Georgia", 15))


            #back buton duh
            self.manager_home_button = tk.Button(self.manager_bottom, text = 'Home',
                                        command = self.Go_home)

            self.main_title.pack()
            self.managername.pack()
            self.information.pack(pady = 10)
            self.manager_home_button.pack()
            #self.num_of_users.pack(pady = 10)

    def Go_home(self):
        self.manager_page.pack_forget()
        self.manager_bottom.pack_forget()
        self.cancel_reservation.pack_forget()
        self.main.pack()
    #--------------------------------------------------------------------------------------------------#               
    
    #--------------------------------------------------------------------------------------------------#
    def CancelBooking(self):
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
        self.cancel_reservation.pack()

        self.main_title = tk.Label(self.cancel_reservation, text = "Cancel Booking", 
                                                            font = ("Georgia", 25), fg= "#578ee6")
        
        self.email = tk.Label(self.cancel_reservation, text = 'Enter Email:')
        self.email_entry = Entry(self.cancel_reservation)
        
        self.room_num = tk.Label(self.cancel_reservation, text = 'Enter Room Number:')
        self.room_num_entry = Entry(self.cancel_reservation)

        self.button_newnext = tk.Button(self.cancel_reservation, text = 'next',
                                        command = self.LastNameConf)

        #back buton duh
        self.back_button = tk.Button(self.cancel_reservation, text = 'Home',
                                        command = self.Go_home)

        ### in the window
        self.main_title.pack()
        self.email.pack()
        self.email_entry.pack()

        self.room_num.pack()
        self.room_num_entry.pack()
 
        self.button_newnext.pack()
        #printing back button
        self.back_button.pack()
        #On the window
    

    def LastNameConf(self):
        """
        Date:August 8, 2022

        Programmer:Phone Pyae Zaw/Mithell Berbera

        Checks if last name is in the database from the entry from CancelBooking Method

        This method will check if the last name is in the database and will print out an error if it is non-existent.
        Parameters:
        None

        Returns:
        None
        """
        #gets the email and room number from the entry box that the user put
        self.email_conf = self.email_entry.get()
        self.room_conf = self.room_num_entry.get()

        #checks to see if the room is first a actually room, and then also if the room needs to be cancelled
        with open('user_data.csv', 'r') as f:
            self.reader = f.read()
            if (self.email_conf, self.room_conf in self.reader):
                #sends the info to check the datafiles 
                self.answer = Database.cancel_room(self,self.room_conf,self.email_conf)
                if(self.answer == 0):
                    #if the database does not have email and room number in the data then it will return a 0 which runs this
                    self.ConfNum2 = tk.Label(self.cancel_reservation, text = "This room doesn't exist.")
                    self.ConfNum2.pack()
                elif(self.answer == 1):
                    #if the database sees that the room is available then it will return a 1 which runs this
                    self.ConfNum3 = tk.Label(self.cancel_reservation, text = "This room is already available. No need to cancel.")
                    self.ConfNum3.pack()
                elif(self.answer == 2):
                        print("You have cancelled your booking.")
                        self.canceltext = tk.Label(self.cancel_reservation, text = "You have cancelled your booking.")
                        self.canceltext.pack()

                        

                #Customer.name(self)
            else:
                self.ConfNum = tk.Label(self.cancel_reservation, text = 'Error')
                self.ConfNum.pack()
                self.cancel_reservation.pack_forget()
                #self.cancel_reservation.pack_forget()
    #--------------------------------------------------------------------------------------------------#

    #--------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    """Calls the main class."""
    base = HotelGUI()
