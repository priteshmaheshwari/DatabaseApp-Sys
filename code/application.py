

#importing dependencies

import os
import re
import database
import numpy as np
import pandas as pd
from datetime import datetime
from tabulate import tabulate
import webbrowser
from database import databaseQueries



def runApplication(user_name):
    '''
    Function to take the inputs to the applicationn and accessing the database
    
    '''
    print('Select Which Query to run')
    
    choice = None
    
    #prsenting the choices to the user

    while True:
        print('''
Query 1:
Hospital Information according to Zip code with Google Maps location.
    
Query 2:
Giving all information available for Covid cases in a particular county and date range.

Query 3:
First shows the NAICS Code and its description then asks the user choose the NAICS code.
Then Giving a list of all hospitals with address for a particular NAICS code and ZIP code.

Query 4:
The date a hospital was last reviewed in a particular zip code

Query 5:
The sum of deaths and number of hospitals and Average deaths per hospitalin a particular county 

To exit:
Press 0
''')
        choice = int(input("Enter the option you would like to access ==> "))
        _ = None
        if choice == 0:
            break
        elif choice == 1:
            
            x = databaseQueries.query1(_, user_name)
            #code for displaying the google maps links
            locations = []
            for i in x.iterrows():
                temp = list(i[1])
                y = (temp[3].split(' '))
                y = "%20".join(y)
                temp = y+'%20'+temp[4]+'%20'+temp[6]+'%20'+str(temp[7])
                print("http://www.google.com/maps/place/" +  temp.lower())
        elif choice == 2:
            
            databaseQueries.query2(_, user_name)
        elif choice == 3:
            databaseQueries.query3(_, user_name)
        elif choice == 4:
            databaseQueries.query4(_, user_name)
        elif choice == 5:
            databaseQueries.query5(_, user_name)
        


if __name__ == "__main__":
    _ =None
    '''
    Main Driver code of the application
    '''
#     connection_string = "user='nyc_covid' password='nyc_covid' dbname='nyc_covid' "
#login & sign up 
    print('''Welcome to Exploring Hospital and COVID-19 Data Application''')
    while True:
        choice = None
        print('''
To Login Press 1
                 
For Registration Press 2

To exit Press 0
                ''')
        try:
            choice = int(input())
            if choice == 0:
                break
            elif choice == 1:
                user_name = str(input('Enter User Name ==> '))
                ret_val = databaseQueries.login(user_name)
                if ret_val == 1:
                    runApplication(user_name)
                elif ret_val == -1:
                    print("Error")
                    continue
                else:
                    print('User Not Found')
                    continue
                    
                break
                
            elif choice == 2:
                user_name = str(input("Enter User Name to be create ==> "))
                ret_val = database.databaseQueries.register(_,user_name)
                if ret_val == 0:
                    print("User Name Already Exists")
                elif ret_val == 1:
                    
                    print("User Name Created!")
                    runApplication(user_name)
                elif ret_val == -1:
                    print("Error")
                    continue
                break
            else:
                print('Incorrect Choice')
                continue
         # Error handling  
        except Exception as error:
            

            print ("Oops! An exception has occured:", error)
            print ("Exception TYPE:", type(error))
            break
        
        
