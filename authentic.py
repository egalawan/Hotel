def welcome():
    print("Welcome to Hotel Scrummy, the Hotel for all your needs")
    answer = input("New User or Login(no caps): ")
    if answer == 'new user':
        print("hello")
welcome()
def register():
    db = open("HotelRooms.txt", "r")
    
    Username = input("Create username: ")
    Password = input ("Create password: ")
    Password2 = input ("Confirm password: ")

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
            db.write(Username + ", " + Password + "\n")
            print("Success!")
register()

def access():
    pass