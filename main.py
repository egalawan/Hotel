from tkinter import *

# Creates a window
window = Tk()
window.geometry("420x420")
window.title("Hotel Scrummy")

# Creates a title for our window
label = Label(window,
              text="Welcome to Hotel Scrummy.",
              font=("Arial", 16, "bold"),
              fg="#669eff")
label.pack()

# Creates a button for viewing inventory
button = Button(window,
                text="View available rooms",
                font=("Arial", 14))
button.pack()

# Creates a button for cancelling a reservation
button = Button(window,
                text="Cancel reservation",
                font=("Arial", 14))
button.pack()

# Displays the window
window.mainloop()