def welcome():
    print("Welcome to Hotel Scrummy, the Hotel for all your needs")
    answer = input("New User(1) or Login(2): ")
    if answer == '1':
        print("Hello New User")
    else:
        print("Welcome Back User")
        UserName2 = input("Please Enter Username: ")
        with open("HotelRooms.txt", "r") as file:
         size = 100
         FileNames = file.read(size)
         while len(FileNames) > 0:
            print(FileNames, end = '')
            FileNames = file.read(size)

with open("HotelRooms.txt", "r") as file:
         size = 100
         FileNames = file.read(size)
         while len(FileNames) > 0:
            print(FileNames, end = '')
            FileNames = file.read(size)        
welcome()
def register():
    FullName = input("Insert First Name and Last name: ")
    Username = input("Create username: ")
    Password = input ("Create password: ")
    Password2 = input ("Confirm password: ")
    RoomNumber = input ("Which Room would you like: ")
    if Password != Password2:
        print("Passwords dont match, restart")
        register()
    else:
        if len(Password) <= 6:
            print("Password too short, restart")
            register()
        #elif Username in db:
        #    print("Username exists, enter different password")
        #   register()
        else:
            db = open("HotelRooms.txt", "a")
            db.write(FullName + "     " + Username + "       " + Password + "       " + RoomNumber + "\n")
            print("Success!")
register()
print("Thank you for visiting")

def access():
    pass