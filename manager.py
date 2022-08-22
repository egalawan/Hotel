import pandas as pd
class Manager():
    def show_report(self):
        #gets the information from the file then sends it back to the main
        df = pd.read_csv("user_data.csv")
        df2 = df.to_string(index=False)
        return df2

        ##we can have multiple managers with different passwords if we need?

    def manager(self,password):
        self.password_set = {'6728','8930'}
        #user sends password and then we see if the password is real first
        if password not in self.password_set:
            return "no password"
        #selects manager based on which password they put
        elif password == '6728':
            manager = "Joe Paskado"
            return(manager)
        
        elif password == '8930':
            manager = "Sergio Ramiro"
            return(manager)

        
