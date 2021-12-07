import os
import pandas as pd
from os import walk
import psycopg2
from psycopg2 import sql
from psycopg2.sql import Identifier, SQL
from datetime import datetime
import numpy as np
from tabulate import tabulate
from sqlalchemy import create_engine
import re
#import lxml
import psycopg2.extras

connection_string = "user='nyc_covid' password='nyc_covid' dbname='nyc_covid' "
conn = psycopg2.connect(connection_string)


class databaseQueries():

    def __init__():

        conn = psycopg2.connect(connection_string)    
        
        
        
    def login_counter(user_name):
        '''
        Count Number of times user logged in 
        '''
        cursor = conn.cursor()
        query = ("""SELECT * FROM user_data WHERE user_name = %s""")
        cursor.execute(query, (user_name,))
        records = cursor.fetchall()
        if len(records) == 0:
            log_count = 1
        elif len(records) == 1:
            log_count = records[0][1] + 1
        return log_count
    
    def login(user_name):
        '''
        logs user entry
        '''
        try:
            cursor = conn.cursor()
            query = ("""Select user_name from user_data""")
            cursor.execute(query)
            records = cursor.fetchall()
            if user_name in [i[0] for i in records]:
                log_count = databaseQueries.login_counter(user_name) 
                query = ("""UPDATE user_data SET login_count = %s WHERE user_name = %s;""") 
                cursor.execute(query, (log_count,user_name)) 
                conn.commit() 
                return 1
            else:
                return 0           
        except Exception as error:
            print ("Oops! An exception has occured:", error)
            print ("Exception TYPE:", type(error))
            return -1
    def register(user_name):
        try:         
            cursor = conn.cursor()
            query = ("""Select user_name from user_data""")
            cursor.execute(query)
            records = cursor.fetchall()
            if user_name in [i[0] for i in records]:
                
                return 0
            else:
                #cursor = conn.cursor()
                log_count = databaseQueries.login_counter(user_name) 
                query = ("""INSERT INTO user_data(user_name,login_count) VALUES (%s,%s);""")
                cursor.execute(query, (user_name,log_count)) 
                conn.commit()
                return 1
        except Exception as error:
            print ("Oops! An exception has occured:", error)
            print ("Exception TYPE:", type(error))
            return -1
        
        
    def query1(self):
        
        '''
         QUERY 1 : Hospital Information according to Zip code (with Google Maps location, maybe)
         Input: Zip code (INT)
         Output: Pandas Dataframe / table
         reutrns df
         '''
        # try:
        zip_code = int(input("Enter a 5 digit Zip Code to retrive Hospital Information==>"))
            
        # except:
        #     print("Incorrect ZIP code")
            
        try:
            cursor = conn.cursor()
    #         print('test')
    
            query = ('''SELECT h.objectid, h.id, h.name, a.address, a.city, a.county, a.state, a.zip, a.latitude, a.longitude, h.type, c.telephone, c.website \
            FROM hospital_data h JOIN address_data a ON h.objectid = a.objectid \
            AND h.id = a.id JOIN contact_data c ON h.objectid = c.objectid AND h.id = c.id \
            WHERE a.zip = {c1};''').format(c1=zip_code)
            cursor.execute(query)
            records = cursor.fetchall()
            headers = ['ObjectID', 'ID', 'Name', 'Address', 'City', 'County', 'State', \
                        'ZIP', 'Latitude','Longitude', 'Type', 'Telephone', 'Website' ]
    #         print(records)
            table = []
            
            for i in records:
                
                
                table.append([i[0], i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12]])
            df = pd.DataFrame(table, columns = headers)  
    #         print(table)
    #         table = [[records[i][0], records[i][1], records[i][2], records[i][3], records[i][4], records[i][5],records[i][6],records[i][7],records[i][8],records[i][9],records[i][10],records[i][11], records[i][12],records[i][13] ]]
            print(tabulate(table, headers))  
    #         print(df)
            return df
        except:
            print("Something went wrong2")
            return
            
            
            
            
            
            
            
            
            
            
            
    def query2(self):
        '''
             QUERY 2 : Giving all information avalable for Covid cases in a particular county and date range
             Input: county,start date, end date
             Output: Pandas Dataframe /table
        '''
        
        try:
            county = str(input('Input county to check for all information avalable for Covid cases from Jan to Oct 2021 ==> ')).lower().strip()
            year = 2021
            s_month = int(input('Input a START month between 1-10 ==> ').strip())
            s_day = int(input('Input a START date between 1-31 ==> ').strip())
            e_month = int(input('Input a END month between 1-10 ==> ').strip())
            e_day = int(input('Input a END date between 1-31 ==> ').strip())
            m_31 = [1,3,5,7,8,10]
            m_30 = [2,4,6,9]
            
            if s_month in m_31:
                if 0< s_day <= 31:
                    s_date = str(year) + '-' + str(s_month) + '-' + str(s_day)
                elif 0< s_day <= 31:
                    s_date = str(year) + '-' + str(s_month) + '-' + str(s_day)
                else:
                    raise Exception('DATE out of range')
                    
            elif s_month in m_30:
                if 0 < s_day <= 30:
                    s_date = str(year) + '-' + str(s_month) + '-' + str(s_day)
                
                elif 0 < s_day <= 30:
                    s_date = str(year) + '-' + str(s_month) + '-' + str(s_day)
                
                else:
                    raise Exception('DATE out of range')
            if e_month in m_31:
                if 0< e_day <= 31:
                    e_date = str(year) + '-' + str(e_month) + '-' + str(e_day)
                elif 0< e_day <= 31:
                    e_date = str(year) + '-' + str(e_month) + '-' + str(e_day)
                else:
                    raise Exception('DATE out of range')
                    
            elif e_month in m_30:
                if 0 < e_day <= 30:
                    e_date = str(year) + '-' + str(e_month) + '-' + str(e_day)
                elif 0 < e_day <= 30:
                    e_date = str(year) + '-' + str(e_month) + '-' + str(e_day)
                else:
                    raise Exception('DATE out of range')
            else:
                raise Exception('MONTH out of range')
        
        
        except :
            print("Incorrect Date(s)")
            return 
            
            
        
        try:
            cursor = conn.cursor()
    #         print('test')
    
            query = ('''SELECT date, state, cases, cases_avg, cases_avg_per_100k, deaths, deaths_avg, deaths_avg_per_100k \
                        FROM counties WHERE LOWER(COUNTY) = %s AND DATE BETWEEN %s AND %s;''')
    #         print('till here fine')
            cursor.execute(query, (str(county), str(s_date), str(e_date)))
            
    
            records = cursor.fetchall()
    #         print(records)
            headers = ['Date', 'State', 'Cases', 'Cases_Avg', 'Cases_Avg_per_100k ', 'Deaths', 'Deaths_Avg','Deaths_Avg_per_100k']
    #         print(records)
            table = []
            
            
            for i in records:
                
                table.append([i[0], i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
    #         print(table)
            df = pd.DataFrame(table) 
            df.columns = headers
            print(tabulate(table, headers)) 
            return df
        except Exception as error:
            print ("Oops! An exception has occured:", error)
            print ("Exception TYPE:", type(error))
            return
            
         
            
         
            
         
            
            
            
    def query3(self):
        '''
             QUERY 3 : First show the NAICS Code and its description then make the user choose the NAICS code
             Then - Giving a list of all hospitals with address for a particular NAICS code and ZIP code
             Input: NAICS CODE,  ZIP CODE
             Output: Pandas Dataframe / table
        '''
        cursor = conn.cursor()
        query =('''SELECT DISTINCT(NAICS_CODE), NAICS_DESC FROM hospital_data;''')
        cursor.execute(query)
        records = cursor.fetchall()
        headers = ['NAICS Codes', 'NAICS Description']
        
        table = []
       
        for i in records:
            table.append([i[0], i[1]])
        df = pd.DataFrame(table, columns = headers) 
        print(tabulate(table, headers))  
        print('''
                Enter a NAICS Code from the above table to view all hospitals 
                with address for a that particular NAICS code and ZIP code.
                ''')
        try:
            Naics_code = int(input('Enter a NAICS Code from the above table ==> ').strip())
            zip_code = int(input('Enter a zip code to view all hospitals ==> ').strip())
        #         print(df['NAICS Codes'])
            if Naics_code not in list(df['NAICS Codes']):
                raise Exception('NAICS Code not in above list')
            query =('''SELECT h.objectid, h.id, h.name, h.type, h.beds, a.address, a.city, a.county, a.state, a.zip, a.latitude, a.longitude \
                        FROM hospital_data h JOIN address_data a ON h.objectid = a.objectid AND h.id = a.id \
                        WHERE a.zip = {};''').format(zip_code)
            cursor.execute(query)
            records = cursor.fetchall()
            headers = ['ObjectID', 'ID', 'Name','Type', 'Address', 'City', 'County', 'State', \
                        'ZIP', 'Latitude','Longitude']
            table = []
            for i in records:
                table.append([i[0], i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]])
            df = pd.DataFrame(table, columns = headers)
            print(tabulate(table, headers)) 
            return df
        
        
        
        except Exception as error:
            print ("Oops! An exception has occured:", error)
            print ("Exception TYPE:", type(error))
            return
        #     try:
        #         NAICS_Code = int(input(''))
        
        
        









    def query4(self):
        '''
             QUERY 4 : The date a hospital was last reviewed in a particular zip code
             Input: ZIP CODE
             Output: Pandas Dataframe / Table
        '''
        try:
            cursor = conn.cursor()
            zip_code = int(input('Enter a zip code to view all hospitals ==> ').strip())
            query =('''SELECT h.objectid, h.id, h.name, h.status, h.type, h.trauma, h.owner, h.ttl_staff, h.population, h.beds, h.helipad, m.source, m.sourcedate, m.val_method, m.val_date, a.zip \
                        FROM hospital_data h JOIN metadata m ON h.objectid = m.objectid \
                        AND h.id = m.id JOIN address_data a ON h.objectid = a.objectid \
                        AND h.id = a.id WHERE a.zip = {};''').format(zip_code)
            cursor.execute(query)
            records = cursor.fetchall()
            headers = ['ObjectID', 'ID', 'Name','Status','Type', 'Trauma', 'Owner', 'TTL_staff', 'Population','Beds', 'Helipad', 'Source', 'Source Date', 'Val Method','Val Date',  \
                        'ZIP']
            table = []
            for i in records:
                table.append([i[0], i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],])
            df = pd.DataFrame(table, columns = headers)
            print(tabulate(table, headers))
            return df
        except Exception as error:
            print ("Oops! An exception has occured:", error)
            print ("Exception TYPE:", type(error))

    







    def query5(self):
        '''
             QUERY 5 : The sum of deaths and number of hospitals in a particular county
             Input: COUNTY 
             Output: SUM & count 
        '''
        try:
            cursor = conn.cursor()
            county = str(input('Input county to check for all information avalable for Covid cases from Jan to Oct 2021 ==> ')).lower()
            query_1 =('''SELECT SUM(c.deaths), LOWER(c.county), c.state \
                        FROM counties c GROUP BY c.county, c.state \
                        HAVING LOWER(c.county) = %s ORDER BY c.county, c.state;''')
            cursor.execute(query_1, [county])
            records_1 = cursor.fetchall()
            
            
            query_2 =('''SELECT COUNT(a.id),LOWER(a.county), a.state FROM address_data a \
                        GROUP BY a.county, a.state HAVING LOWER(a.county) = LOWER(%s) \
                        ORDER BY a.county, a.state;''')
            cursor.execute(query_2, [county])
            records_2 = cursor.fetchall()
            
            # print(records_2)
            
            headers = ['Total Number of Deaths', 'County', 'State']
            table = []
            for i in records_1:
                table.append([i[0], i[1],i[2]])
            df = pd.DataFrame(table, columns = headers)
            
            headers_2 = ['Total Number of Hospitals', 'County', 'State']
            table_2 = []
            for i in records_2:
                table_2.append([i[0], i[1],i[2]])
            df_2 = pd.DataFrame(table_2, columns = headers_2)
            d = {'Total Number of Deaths': df['Total Number of Deaths'], 'Total Number of Hospitals' : df_2['Total Number of Hospitals'],'Deaths / Hospial': df['Total Number of Deaths'] / df_2['Total Number of Hospitals'], 'County': df['County'], 'State': df['State'] }
            df = pd.DataFrame(d)
            print(df)
        except Exception as error:
            print ("Oops! An exception has occured:", error)
            print ("Exception TYPE:", type(error))
































# =============================================================================
# if __name__ == "__main__":
#     x=None
    
#     databaseQueries.register('121')
    
# =============================================================================
         