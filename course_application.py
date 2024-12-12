import os
import pandas as pd
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# environment variables get
load_dotenv()

# environment variables set
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')



def fetch_data():
    
    try:
        # secure connection to the database
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
            # query to fetch the required fields
        query = """SELECT 
                a.program, 
                a.email, 
                 c.course_name, 
               t.applying_level, 
               t.current_level, 
              c.fee_details, 
              ap.application_status 
             FROM 
              Account a 
              INNER JOIN Term_course_registration_application t ON a.id = t.account_id 
             INNER JOIN Application ap ON t.application_id = ap.id 
             INNER JOIN Course c ON t.course_id = c.id;
            """

            # fetch the data into a pandas DataFrame
        data_frame = pd.read_sql(query, connection)
        return data_frame

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Database connection closed.")

# Fetch the data and display the DataFrame


data = fetch_data()

if data is not None:
    print(data.head())

