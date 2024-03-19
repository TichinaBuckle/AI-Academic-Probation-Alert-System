# Group Members: - Tichina Buckle, Micah Brown, Robert Ramone, Winston
# Date Last Updated: 3-19-2024
# File Name: Functions.py
# Description:

import mysql.connector
import DatabaseConnection

# Student CRUD Functions

# Create / Add Student to database
def CreateStudent():
    conn = DatabaseConnection()
    cursor = conn.cursor()
    cursor.excute("Insert INTO student_master (student_id, student_name, student_email, school, programme) VALUES (%d, %s, %s, %s, %s)")
    conn.commit()