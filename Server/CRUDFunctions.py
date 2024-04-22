# Group Members: - Tichina Buckle, Micah Brown, Ramoune Roberts, Winston
# Date Last Updated: 3-19-2024
# File Name: CRUDFunctions.py
# Description: Stores the Basic CRUD Functions

import logging
import mysql.connector
import DatabaseConnection

# Configure logging
logging.basicConfig(filename='application.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Student CRUD Functions

# Create / Add Student to database
def CreateStudent(studentID, studentName, studentEmail, school, programme):
    conn = DatabaseConnection.DatabaseConnection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO student_master (student_id, student_name, student_email, school, programme) VALUES (%s, %s, %s, %s, %s)", (studentID, studentName, studentEmail, school, programme))
        conn.commit()
        logging.info("Student Added successfully!")
    except Exception as e:
        logging.error(f"Error Adding Student: {e}")
    finally:
        cursor.close()
        conn.close()

# Read specific student data from database
def ReadStudent(studentID):
    conn = DatabaseConnection.DatabaseConnection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM student_master WHERE student_id = %s", (studentID,))
        student = cursor.fetchone()
        if student is None:
            logging.info("Student not found.")
        else:
            logging.info(f"Student Found: {student}")
    except Exception as e:
        logging.error(f"Error Finding Student: {e}")
    finally:
        cursor.close()
        conn.close()

# Retrieved all students from database
def StudentList():
    conn = DatabaseConnection.DatabaseConnection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM student_master")
        students = cursor.fetchall()
        for student in students:
            logging.info(student)
    except Exception as e:
        logging.error(f"Error Fetching Students: {e}")
    finally:
        cursor.close()
        conn.close()

# Update student data in database
def UpdateStudent(studentID, studentName, studentEmail, school, programme):
    conn = DatabaseConnection.DatabaseConnection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE student_master SET student_name = %s, student_email = %s, school = %s, programme = %s WHERE student_id = %s", (studentName, studentEmail, school, programme, studentID))
        conn.commit()
        logging.info("Student Updated successfully!")
    except Exception as e:
        logging.error(f"Error Updating Student: {e}")
    finally:
        cursor.close()
        conn.close()

# Delete Student from database
def DeleteStudent(studentID):
    conn = DatabaseConnection.DatabaseConnection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM student_master WHERE student_id = %s", (studentID,))
        conn.commit()
        logging.info("Student Deleted successfully!")
    except Exception as e:
        logging.error(f"Error Deleting Student: {e}")
    finally:
        cursor.close()
        conn.close()

# CRUD Functions for Module

# Create / Add Module to database
def CreateModule(module, numberOfCredit):
    conn = DatabaseConnection.DatabaseConnection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO module_master (module, number_of_credit) VALUES (%s, %s)", (module, numberOfCredit))
        conn.commit()
        logging.info("Module Added successfully!")
    except Exception as e:
        logging.error(f"Error Adding Module: {e}")
    finally:
        cursor.close()
        conn.close()

# Read specific module data from database
def ReadModule(module):
    conn = DatabaseConnection.DatabaseConnection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM module_master WHERE module = %s", (module,))
        module = cursor.fetchone()
        if module is None:
            logging.info("Module not found.")
        else:
            logging.info(f"Module Found: {module}")
    except Exception as e:
        logging.error(f"Error Finding Module: {e}")
    finally:
        cursor.close()
        conn.close()

# Retrieved all modules from database
def ModuleList():
    conn = DatabaseConnection.DatabaseConnection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM module_master")
        modules = cursor.fetchall()
        for module in modules:
            logging.info(module)
    except Exception as e:
        logging.error(f"Error Fetching Modules: {e}")
    finally:
        cursor.close()
        conn.close()

# Update module data in database
def UpdateModule(module, numberOfCredit):
    conn = DatabaseConnection.DatabaseConnection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE module_master SET number_of_credit = %s WHERE module = %s", (numberOfCredit, module))
        conn.commit()
        logging.info("Module Updated successfully!")
    except Exception as e:
        logging.error(f"Error Updating Module: {e}")
    finally:
        cursor.close()
        conn.close()

# Delete Module from database
def DeleteModule(module):
    conn = DatabaseConnection.DatabaseConnection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM module_master WHERE module = %s", (module,))
        conn.commit()
        logging.info("Module Deleted successfully!")
    except Exception as e:
        logging.error(f"Error Deleting Module: {e}")
    finally:
        cursor.close()
        conn.close()

# CRUD Functions for Module Detail

# Create / Add Module Detail to database
def CreateModuleDetail(module, year, semester, studentId, gradePoint):
    conn = DatabaseConnection.DatabaseConnection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO module_detail (module, year, semester, student_id, grade_point) VALUES (%s, %s, %s, %s, %s)", (module, year, semester, studentId, gradePoint))
        conn.commit()
        logging.info("Module Detail Added successfully!")
    except Exception as e:
        logging.error(f"Error Adding Module Detail: {e}")
    finally:
        cursor.close()
        conn.close()

# Read specific module detail from database
def ReadModuleDetail(id):
    conn = DatabaseConnection.DatabaseConnection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM module_detail WHERE id = %s", (id,))
        module_detail = cursor.fetchone()
        if module_detail is None:
            logging.info("Module Detail not found.")
        else:
            logging.info(f"Module Detail Found: {module_detail}")
    except Exception as e:
        logging.error(f"Error Finding Module Detail: {e}")
    finally:
        cursor.close()
        conn.close()

# Retrieved all modules details from database
def ModuleDetailList():
    conn = DatabaseConnection.DatabaseConnection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM module_detail")
        module_details = cursor.fetchall()
        for module_detail in module_details:
            logging.info(module_detail)
    except Exception as e:
        logging.error(f"Error Fetching Module Details: {e}")
    finally:
        cursor.close()
        conn.close()

# Update module detail in database
def UpdateModuleDetail(id, module, year, semester, studentId, gradePoint):
    conn = DatabaseConnection.DatabaseConnection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE module_detail SET module = %s, year = %s, semester = %s, student_id = %s, grade_point = %s WHERE id = %s", (module, year, semester, studentId, gradePoint, id))
        conn.commit()
        logging.info("Module Detail Updated successfully!")
    except Exception as e:
        logging.error(f"Error Updating Module Detail: {e}")
    finally:
        cursor.close()
        conn.close()

# Delete Module Detail from database
def DeleteModuleDetail(id):
    conn = DatabaseConnection.DatabaseConnection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM module_detail WHERE id = %s", (id,))
        conn.commit()
        logging.info("Module Detail Deleted successfully!")
    except Exception as e:
        logging.error(f"Error Deleting Module Detail: {e}")
    finally:
        cursor.close()
        conn.close()
