# Group Members: - Tichina Buckle, Micah Brown, Ramoune Roberts, Winston
# Date Last Updated: 3-19-2024
# File Name: CRUDFunctions.py
# Description: Stores the Basic CRUD Functions

import mysql.connector
import DatabaseConnection

# Student CRUD Functions

# Create / Add Student to database
def CreateStudent(studentID, studentName, studentEmail, school, programme):
    conn = DatabaseConnection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO student_master (student_id, student_name, student_email, school, programme) VALUES (%d, %s, %s, %s, %s)", (studentID, studentName, studentEmail, school, programme))
        conn.commit()
        print("Student Added successfully!")
    except Exception as e:
        print(f"Error Adding Student: {e}")
    finally:
        cursor.close()
        conn.close()