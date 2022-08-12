import tkinter as tk
#from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import csv
from csv import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from customer import Customer

class HotelGUI():
     #Attributes - Fields
     #Constructors
    
    #--------------------------------------------------------------------------------------------------#
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hotel Scrummy")
        #self.window.configure(bg = '#458B74')
        self.window.geometry('420x420')

        #Creating each 'window' space for the information
        self.main = tk.Frame(self.window)
        self.LogIn = tk.Frame(self.window)
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
        #Labels for main Window
        #Main Window Start
        self.main.pack(side = TOP)

        #self.canvas_ = Canvas(self.main, width=250, height=250)
        

        self.welcome_text = tk.Label(self.main, text ="Welcome to Hotel Scrummy",
                                                font = ("Georgia", 20), fg= "#578ee6")

        self.Info_text = tk.Label(self.main, text ="from Team Damp",
                                                font = ("Times New Roman", 15), fg= "#ffb3e9")
                                                


        self.buttonLogin = tk.Button(self.main, text = 'Log In',
                                                      activebackground = 'green',
                                                      foreground= "green",
                                                      command = self.OpenLogin)

        self.buttonRegister = tk.Button(self.main, text = 'Register', 
                                        command = self.OpenRegister)
        
        self.buttonOpenRooms = tk.Button(self.main, text = 'Available rooms', 
                                        command = self.OpenRooms)

        self.buttonModify = tk.Button(self.main, text = 'Edit Reservation', 
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
        
        #was trying to change the colors of each of the buttons and labels but didnt work
        #self.welcome_text.configure(bg = '#458B74')
        #self.buttonLogin.configure(bg = 'red')
        #self.buttonRegister.configure(bg = '#458B74')
        #self.buttonOpenRooms.configure(bg = '#458B74')
        #self.buttonModify.configure(bg = '#458B74')
        

        #Main Window Page with all the functions to show the order on the page
        #.pack and .pack() are like the printing on the gui,
        #there are different ways to print .pack makes it a little easier to place
        #the buttons and labels next to each other
        
        self.labelImage.pack()

        #self.canvas_.pack(row = 5, column = 1)
        self.welcome_text.pack()
        self.Info_text.pack(pady= 5)

        #buttons on main window in order
        self.buttonLogin.pack(side = LEFT, expand=True, fill = 'x')
        self.buttonRegister.pack(side = TOP, expand=True, fill = 'x')
        self.buttonOpenRooms.pack(side = TOP, expand=True, fill = 'x')
        self.buttonModify.pack(side = TOP, expand=True, fill = 'x')
        button_quit.pack(side = BOTTOM, expand=True)
        
    #--------------------------------------------------------------------------------------------------#
    def OpenLogin(self):
        #deleting the previouse packs so that it switches 'frames'
        
        self.main.pack_forget()
        #calling on the new frame which is the LogIn Page
        self.LogIn.pack()
        
        #Inside the OpenLogin Window Now##
        self.LogInMessage = tk.Label(self.LogIn, text ="Welcome Back User",
                                                 font = ("Times New Roman",30))
        
        
        #creating spots for the user to be able to put in information
        self.User_name = tk.Label(self.LogIn, text = 'Username:')
        self.Username_entry = Entry(self.LogIn)
        
        #confirm button
        self.button_next = tk.Button(self.LogIn, text = 'Next',
                                        command = self.CheckLogin)

        #back buton duh
        self.back_button = tk.Button(self.LogIn, text = 'back',
                                        command = self.Go_back)


        ######need to work on storing the username and password information

        self.Pass_word = tk.Label(self.LogIn, text = 'Password:')
        self.Password_entry = Entry(self.LogIn, show = "*")
        
        ##printing username and password on the LogIn page using .pack()??
        self.LogInMessage.pack()

        self.User_name.pack()
        self.Username_entry.pack()

        self.Pass_word.pack()
        self.Password_entry.pack()

        
        #printing back button
        self.button_next.pack()
        self.back_button.pack()
        

        ####### end of OpenLogin Window
    #--------------------------------------------------------------------------------------------------#
    
    #--------------------------------------------------------------------------------------------------#
    def CheckLogin(self):
        self.LogIn.pack_forget()
        ##for when logging in and need to check if information is correct and in other database
        ##if information isnt on the database, need to ask user to re-enter or to make a new account
        # used for command
        #  
    #--------------------------------------------------------------------------------------------------#
   
    #--------------------------------------------------------------------------------------------------#
    def Go_back(self):
        #'forgetting each of the last pages
        self.LogIn.pack_forget()
        self.RegisterNewUser.pack_forget()
        self.ViewAvailableRooms.pack_forget()
        self.ModifyReservation.pack_forget()
        #adding the main page

        self.main.pack()
    
    #--------------------------------------------------------------------------------------------------#
    
    #saving and sending information from user entry's
    #--------------------------------------------------------------------------------------------------#
    #arrray to keep the entry information from the user
    names_list=[]

    #retrieving the information from the entry box
    def Add(self):
        self.list=[self.fullname_entry.get(),
                 self.Username_entry.get(),
                 self.newPassword_entry.get()]
        self.names_list.append(self.list)
    
    #sending the information to the database file 
    def send_UserInfo(self):
        ##opening the data base to input information
        with open('user_data.csv', 'a') as file:
            Writer = writer(file)
            Writer.writerows(self.names_list)
        


    #--------------------------------------------------------------------------------------------------#
   ##SIGN UP PAGE
    #--------------------------------------------------------------------------------------------------#
    def OpenRegister(self):
        self.main.pack_forget()

        #deleting the previous page and switching 'frames' 
        self.RegisterNewUser.pack()
        
        #Inside the OpenLogin Window Now##
        self.LogInMessage = tk.Label(self.RegisterNewUser, text ="Sign Up",
        font = ("Times New Roman", 30))
        
        
        #creating spots for the user to be able to put in information
        self.full_name = tk.Label(self.RegisterNewUser, text = 'Enter First and Last Name:')
        self.fullname_entry = Entry(self.RegisterNewUser)
        
        ######need to work on storing the username and password information

        self.Username_ = tk.Label(self.RegisterNewUser, text = 'Create a Username:')
        self.Username_entry = Entry(self.RegisterNewUser)

        self.newPassword_ = tk.Label(self.RegisterNewUser, text = 'Create a Password:')
        self.newPassword_entry = Entry(self.RegisterNewUser)

        #buttons to save/which gets the information from the entry box/
        #and button to write on file
        self.button_next = tk.Button(self.RegisterNewUser, text = 'next',
                                        command = self.send_UserInfo)
        
        self.button_save = tk.Button(self.RegisterNewUser, text = 'save',
                                        command = self.Add)
        
        #back buton duh
        self.back_button = tk.Button(self.RegisterNewUser, text = 'back',
                                        command = self.Go_back)

        ### in the window
        self.LogInMessage.pack()
        self.full_name.pack()
        self.fullname_entry.pack()

        self.Username_.pack()
        self.Username_entry.pack()

        self.newPassword_.pack()
        self.newPassword_entry.pack()

        #printing back button
        self.button_save.pack()
        
        self.button_next.pack()
        
        self.back_button.pack()
        
        #On the window
    #--------------------------------------------------------------------------------------------------#
    
    #showing the users all the rooms that are open "inventory"
    #--------------------------------------------------------------------------------------------------#
    def OpenRooms(self):
        self.ModifyReservation.pack_forget()
        self.main.pack_forget()
        self.ViewAvailableRooms.pack()
        self.availableRooms = tk.Label(self.ViewAvailableRooms, text ="Available Rooms",
                                                font = ("Georgia", 20), fg="#578ee6")
        self.availableRooms.pack(pady= 10)
        
        f = open('hotels.csv', 'r')
        with f:
            self.reader = csv.reader(f)
            for row in self.reader:
                print(row)
                for e in row:
                    
                    self.information = tk.Label(self.ViewAvailableRooms, text = row)
                self.information.pack()    
      
                
        ##need to print out the text file with database
        #with open("")
    #--------------------------------------------------------------------------------------------------#
   
   #check user's reservation information, so will need to check the  user database for their information 
   #then check hotel database to see if confirmation number matches a room 

    #--------------------------------------------------------------------------------------------------#
    conf_list = []
    def AddLastName(self):
        self.name_Conf=[self.Lastname_entry.get(),
                 self.ConfNum_entry.get()]
        self.conf_list.append(self.name_Conf)

    ##checking if the last name and the confirmation number in the database is correct
    def LastNameConf(self):
        f = open('room_data.csv', 'r')
        with f:
            self.reader = csv.reader(f)
            if self.name_Conf in self.reader:
                self.ModifyReservation.pack_forget()
                Customer.name(self)
            else:
                self.ConfNum = tk.Label(self.ModifyReservation, text = 'Error')
                self.ModifyReservation.pack_forget()
                self.ConfNum.pack()


    def OpenModify(self):
        self.main.pack_forget()
        self.ModifyReservation.pack()

        self.Lastname = tk.Label(self.ModifyReservation, text = 'Enter Last Name:')
        self.Lastname_entry = Entry(self.ModifyReservation)

        self.ConfNum = tk.Label(self.ModifyReservation, text = 'Enter Confirmation Number:')
        self.ConfNum_entry = Entry(self.ModifyReservation, show = "*")

        self.button_newsave = tk.Button(self.ModifyReservation, text = 'save',
                                        command = self.AddLastName)

        self.button_newnext = tk.Button(self.ModifyReservation, text = 'next',
                                        command = self.LastNameConf)

        #back buton duh
        self.back_button = tk.Button(self.ModifyReservation, text = 'back',
                                        command = self.Go_back)

        ### in the window
        self.Lastname.pack()
        self.Lastname_entry.pack()

        self.ConfNum.pack()
        self.ConfNum_entry.pack()
        self.button_newsave.pack()
        self.button_newnext.pack()
        #printing back button
        self.back_button.pack()
        #On the window
    #--------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    base = HotelGUI()