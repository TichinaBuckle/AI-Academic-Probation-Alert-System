# Group Members: - Tichina Buckle, Micah Brown, Robert Ramone, Winston
# Date Last Updated: 3-19-2024
# File Name: Driver.py
# Description: Test if Functions are working

from CRUDFunctions import CreateStudent

# define student data
studentID = 2101447
studentName = 'Kathy Mattews'
studentEmail = 'kathy.mattews@zmail.com'
school = 'School of Computing and Information Technology'
programme = 'Computing'

# call CreateStudent to add student to database
CreateStudent(studentID, studentName, studentEmail, school, programme)