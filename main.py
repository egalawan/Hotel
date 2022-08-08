import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo

class HotelGUI():
     #Attributes - Fields
     #Constructors
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hotel Scrummy")
        self.window.geometry('420x420')

        #Creating each 'window' space for the information
        self.main = tk.Frame(self.window)
        self.LogIn = tk.Frame(self.window)
        self.RegisterNewUser = tk.Frame(self.window)
        self.ViewAvailableRooms = tk.Frame(self.window)
        self.ModifyReservation = tk.Frame(self.window)

        #Labels for main Window
        #Main Window Start
        self.welcome_text = tk.Label(self.main, text ="Welcome to Hotel Scrummy",
                                                font = ("Times New Roman", 30))


        buttonLogin = tk.Button(self.main, text = 'Log In', 
                                        command = self.OpenLogin)

        buttonRegister = tk.Button(self.main, text = 'Log In', 
                                        command = self.OpenRegister)

        buttonLogin = tk.Button(self.main, text = 'Log In', 
                                        command = self.OpenLogin)
        

        #image
        self.image_file = Image.open("hotel.webp")
        #resize the image
        self.resize = self.image_file.resize((300,300))

        self.my_img = ImageTk.PhotoImage(self.resize)

        #making the label
        self.label = tk.Label(self.main,image=self.my_img)
        self.label.image = self.my_img
        

        #Main Window Page with all the functions to show the order on the page
        self.welcome_text.pack(pady =2)  #pady gives space around text
        self.label.pack()
        buttonLogin.pack()
        
        #quit button
        self.button_quit = tk.Button(self.main, text = 'Exit Greatest Hotel', 
                                                command = self.window.destroy)
        self.button_quit.pack()
        
        self.main.pack()
        self.window.mainloop()
        ##end Main Window

    #Behaviors -Methods

     #switching from self.main to other self.windows
    def OpenLogin(self):
        #deleting the previouse packs so that it switches 'frames'
        self.main.pack_forget()
        #self.label.pack_forget()

        #calling on the new frame which is the LogIn Page
        self.LogIn.pack()

        #Inside the OpenLogin Window Now##
        self.LogInMessage = tk.Label(self.LogIn, text ="Welcome Back User")
        self.LogInMessage.grid(row = 0, column = 0)
        
        #creating spots for the user to be able to put in information
        self.User_name = tk.Label(self.LogIn, text = 'Username:')
        self.Username_entry = Entry(self.LogIn)
        
        #back buton duh
        self.back_button = tk.Button(self.LogIn, text = 'back',
                                        command = self.Go_back)


        ######need to work on storing the username and password information

        self.Pass_word = tk.Label(self.LogIn, text = 'Password:')
        self.Password_entry = Entry(self.LogIn)
        
        ##printing username and password on the LogIn page using .grid()??
        self.User_name.grid(row = 2, column = 0)
        self.Username_entry.grid(row = 3, column = 0)

        self.Pass_word.grid(row = 4, column = 0)
        self.Password_entry.grid(row =5, column = 0)

        #printing back button
        self.back_button.grid(row = 30, column = 1)
        

        ####### end of OpenLogin Window
    def Go_back(self):
        self.LogIn.pack_forget()
        self.main.pack()

    def OpenRegister(self):
        self.main.pack_forget()
        #deleting the previous page and switching 'frames' 
        self.RegisterNewUser.pack()

        #On the window

        
        

if __name__ == "__main__":
    base = HotelGUI()



