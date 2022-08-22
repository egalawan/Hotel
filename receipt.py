import ssl
import smtplib
import pandas as pd
from email.message import EmailMessage

class Receipt():
    def send_email(self, room, email_receiver,name):
        #rooms = {"12":0, "42":1, "11":2, "72":3, "69420":4}
        
        #df =pd.read_csv("user_data.csv")
        self.email_sender = "hotelscrummymgmt@gmail.com"
        self.email_password = "exjcwnwmmqqpzrpy"

        self.subject = "Reservation Details"
        self.body = ("Thank you " + name + " for booking with us, your room number is : " + room)

        self.em = EmailMessage()
        self.em["From"] = self.email_sender
        self.em["To"] = email_receiver
        self.em["Subject"] = self.subject
        self.em.set_content(self.body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, email_receiver, self.em.as_string())