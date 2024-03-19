# Group Members: - Tichina Buckle, Micah Brown, Robert Ramone, Winston
# Date Last Updated: 3-18-2024
# File Name: DatabaseConnection.py
# Description: Connects Application to Database

# libraries Used
import mysql.connector

def DatabaseConnection():
    try:
        # creates connection and fills connection creditials
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="academic_probation_alert_system")

        # checks if connection was successful
        if connection.is_connected():
            print('Connection Successful')
            return connection
        else:
            print('Connection Failed')
            return None
    except Exception as e:
        print("Error Connecting to Server: {e}")
        return None