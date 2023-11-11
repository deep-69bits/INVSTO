import mysql.connector as connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
db =connector.connect(host='localhost',port='3306',user='root',password='deep@6969',database='INVSTO')

cur=db.cursor()



# creating database
# cur.execute("CREATE DATABASE INVSTO")

# creating table
# cur.execute("CREATE TABLE HINDALCO(datetime datetime,close decimal(10,3),high decimal(10,3),low decimal(10,3),open decimal(10,3),volume integer(10),instrument varchar(20))")


# droping table
# cur.execute("DROP TABLE HINDALCO")


df=pd.read_csv('data.csv')
arr = df.to_numpy()


# validation if data is in correct datatype

def validate_data(df):
    # Check if 'Open', 'High', 'Low', 'Close' are decimals
    if not all(df[col].dtype == 'float64' for col in ['open', 'high', 'low', 'close']):
        return False

    # Check if 'Volume' is integer
    if not df['volume'].dtype == 'int64':
        return False

    # Check if 'Instrument' is string
    if not df['instrument'].dtype == 'O':
        return False

    # Check if 'Datetime' is datetime
    if not pd.api.types.is_datetime64_any_dtype(df['datetime']):
        return False

    return True


for i in arr:
    s="INSERT INTO HINDALCO VALUES (%s,%s,%s,%s,%s,%s,%s)"
    b=(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
    cur.execute(s,b)




db.commit()
cur.close()
db.close()