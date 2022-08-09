import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from csv import *
from tkinter import messagebox
from tkinter.messagebox import showinfo

class HotelGUI():
     #Attributes - Fields
     #Constructors
    #arrray to keep the entry information from the user
    main_lst=[]

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hotel Scrummy")
        self.window.configure(bg = '#458B74')
        self.window.geometry('700x700+200+250')

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


        self.buttonLogin = tk.Button(self.main, text = 'Log In', 
                                        command = self.OpenLogin)

        self.buttonRegister = tk.Button(self.main, text = 'Register', 
                                        command = self.OpenRegister)
        
        self.buttonOpenRooms = tk.Button(self.main, text = 'Avalible rooms', 
                                        command = self.OpenRooms)

        self.buttonModify = tk.Button(self.main, text = 'Edit Reservation', 
                                        command = self.OpenModify)
        
        #image
        #self.image_file = Image.open("backgroudphoto.png")
        #resize the image
        #self.resize_image = self.image_file.resize((150,150))

        self.pic_ = Image.open("backgroudphoto.png")
        self.pic_resize = self.pic_.resize((100,100))
        self.my_img = ImageTk.PhotoImage(self.pic_resize)

        #making the label
        self.labelImage = tk.Label(self.main,image=self.my_img)
        self.labelImage.image = self.my_img
        
        #quit button
        button_quit = tk.Button(self.main, text = 'Exit Greatest Hotel', 
                                                command = self.window.destroy)
        

        self.welcome_text.configure(bg = '#458B74')
        self.buttonLogin.configure(bg = 'red')
        self.buttonRegister.configure(bg = '#458B74')
        self.buttonOpenRooms.configure(bg = '#458B74')
        self.buttonModify.configure(bg = '#458B74')
        
        #Main Window Page with all the functions to show the order on the page

        self.labelImage.grid(row = 0, column = 0)
        
        self.welcome_text.grid(row = 1, column = 1) 
        #buttons on main window in order
        self.buttonLogin.grid(row = 3, column = 1)
        self.buttonRegister.grid(row = 4, column = 1)
        self.buttonOpenRooms.grid(row = 6, column = 1)
        self.buttonModify.grid(row = 7, column = 1)
        button_quit.grid(row = 9, column = 1)

        #calling the main page and the labels and buttons assigned to 'main'
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
        
        ##printing username and password on the LogIn page using .grid()??
        self.LogInMessage.grid(row = 0, column = 1)

        self.User_name.grid(row = 3, column = 0)
        self.Username_entry.grid(row = 3, column = 1)

        self.Pass_word.grid(row = 5, column = 0)
        self.Password_entry.grid(row =5, column = 1)

        
        #printing back button
        self.button_next.grid(row=3,column=2)
        self.back_button.grid(row = 5, column = 2)
        

        ####### end of OpenLogin Window

    def CheckLogin(self):
        self.LogIn.pack_forget()

    def Go_back(self):
        self.LogIn.pack_forget()
        self.RegisterNewUser.pack_forget()
        self.ViewAvailableRooms.pack_forget()
        self.ModifyReservation.pack_forget()
        self.main.pack()
    def Add(self):
        self.lst=[self.fullname_entry.get(),self.Username_entry.get(),self.newPassword_entry.get()]
        self.main_lst.append(self.lst)
    
    def save_information(self):
        ##opening the data base to input information
        with open('Database.csv', 'w') as file:
            self.Writer = writer(file)
            self.Writer.writerow(["Name","Age","Contact"])
            self.Writer.writerows(self.main_lst)

            
    def OpenRegister(self):
        self.main.pack_forget()
        #deleting the previous page and switching 'frames' 
        self.RegisterNewUser.pack()

        #Inside the OpenLogin Window Now##
        self.LogInMessage = tk.Label(self.RegisterNewUser, text ="Sign Up")
        self.LogInMessage.grid(row = 0, column = 0)
        
        #creating spots for the user to be able to put in information
        self.full_name = tk.Label(self.RegisterNewUser, text = 'Enter First and Last Name:')
        self.fullname_entry = Entry(self.RegisterNewUser)
        
        ######need to work on storing the username and password information

        self.Username_ = tk.Label(self.RegisterNewUser, text = 'Create a Username:')
        self.Username_entry = Entry(self.RegisterNewUser)

        self.newPassword_ = tk.Label(self.RegisterNewUser, text = 'Create a Password:')
        self.newPassword_entry = Entry(self.RegisterNewUser, show = "*")

        self.button_next = tk.Button(self.RegisterNewUser, text = 'next',
                                        command = self.save_information)
        
        self.button_save = tk.Button(self.RegisterNewUser, text = 'save',
                                        command = self.Add)
        
        #back buton duh
        self.back_button = tk.Button(self.RegisterNewUser, text = 'back',
                                        command = self.Go_back)


        ### in the window
        self.full_name.grid(row=1,column=0)
        self.fullname_entry.grid(row = 1, column = 1)

        self.Username_.grid(row = 3, column = 0)
        self.Username_entry.grid(row =3, column = 1)

        #printing back button
        self.button_next.grid(row = 1, column = 3)
        
        self.button_save.grid(row = 1, column = 2)

        self.back_button.grid(row = 3, column = 2)
        
        #On the window
        

    def OpenRooms(self):
        self.main.pack_forget()
        self.ViewAvailableRooms.pack()

        ##need to print out the text file with database
        #with open("")

    def OpenModify(self):
        self.main.pack_forget()
        self.ModifyReservation.pack()

        self.Lastname = tk.Label(self.RegisterNewUser, text = 'Enter Last Name:')
        self.Lastname_entry = Entry(self.RegisterNewUser)

        self.ConfNum = tk.Label(self.RegisterNewUser, text = 'Enter Confirmation Number:')
        self.ConfNum_entry = Entry(self.RegisterNewUser, show = "*")

        #back buton duh
        self.back_button = tk.Button(self.RegisterNewUser, text = 'back',
                                        command = self.Go_back)

        ### in the window
        self.Lastname.grid(row=1,column=1)
        self.Lastname_entry.grid(row = 2, column = 1)

        self.ConfNum.grid(row = 4, column = 2)
        self.ConfNum_entry.grid(row =5, column = 2)

        #printing back button
        
        self.back_button.grid(row = 9, column = 1)
        #On the window
        

if __name__ == "__main__":
    base = HotelGUI()



