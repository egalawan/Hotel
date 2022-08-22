import pandas as pd
class Manager():
    def show_report(self):
        df = pd.read_csv("user_data.csv")
        df2 = df.to_string(index=False)
        return df2

        ##we can have multiple managers with different passwords if we need?

    def manager(self,which):
        self.password = {'6728','8930'}
        
        if which not in self.password:
            return "no password"

        elif which == '6728':
            manager = "Joe Paskado"
            return(manager)
        
        elif which == '8930':
            manager = "Sergio Ramiro"
            return(manager)

        
