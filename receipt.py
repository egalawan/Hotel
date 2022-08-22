import ssl
import smtplib
import pandas as pd
from email.message import EmailMessage

class Receipt():
    def send_email(self, room, email_receiver,name):
        #email used to send the confirmation to the user
        self.email_sender = "hotelscrummymgmt@gmail.com"
        self.email_password = "exjcwnwmmqqpzrpy"
        #subject of the email
        self.subject_ = "Reservation Details"
        #body of the email telling the user their information for their room
        self.body = (f"Thank you {name} for reserving at Hotel Scrummy. Your room number is: {room}. \n" +
            "We hope you enjoy your room and all of its amenities." + 
            "Please reply to this email with any questions or concerns. We welcome you back at any time. \n" + 
            "Stay scrummy,\n"+
            "Mr. Scrummy of Hotel Scrummy")    
        
        #setting email_vars the method that allows us to send the email with gmail
        self.email_vars = EmailMessage()
        self.email_vars["From"] = self.email_sender
        self.email_vars["To"] = email_receiver
        self.email_vars["Subject"] = self.subject_
        self.email_vars.set_content(self.body)

        context = ssl.create_default_context()
        #the server that sends the email for us
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, email_receiver, self.email_vars.as_string())