granted = False

def grant():
  global granted
  granted = True

def login(name, password) :

  success = False
  file = open("login_Details.txt", "r")
  for i in file:
    a,b = i.split(", ")
    b = b.strip()

    if (a==name and b==password):
      success=True
      break

  file.close()

  if(success):
    print("Login Successful.")
    grant()

  else:
    print("wrong username or password")

def register(name, password):

  file = open("login_details.txt", "a")
  file.write("\n"+name+", "+password)
  file.close()
  grant()

def access(option) :

  global name

  if(option =="login"):
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    login(name, password)
  
  else:
    print("Enter your name and password to register")
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    register(name, password)

def begin():

  global option
  print("Welcome to Hotel Scrummy")
  option = input("Login or Register (login, reg) : ")
  if(option!="login" and option!="reg"):
    begin()

begin()
access(option)

if(granted):
  print("Welcome to Hotel Scrummy")
  print("### User Details ####")
  print("Username: ",name) 