# Group Members: - Tichina Buckle, Micah Brown, Ramoune Roberts, Winston
# Date Last Updated: 3-19-2024
# File Name: Driver.py
# Description: Test if Functions are working

from CRUDFunctions import *

# define student data
studentID = 2101447
studentName = 'Kathy Mattews'
studentEmail = 'kathy.mattews@zmail.com'
school = 'School of Computing and Information Technology'
programme = 'Computing'

# Test for Student
CreateStudent(studentID, studentName, studentEmail, school, programme)
ReadStudent(2101447)
studentEmail = 'kathy.mattews@gmail.com'
UpdateStudent(2101447, 'Kathy Mattews', 'kathy.mattews@gmail.com', 'School of Computing and Information Technology', 'Computing')
ReadStudent(2101447)
#DeleteStudent(2101447)
ReadStudent(2101447)

# define module data
module = 'CS101'
numberOfCredit = 3

# Test for Module
CreateModule(module, numberOfCredit)
ReadModule('CS101')
number_of_credit = 4
UpdateModule('CS101', numberOfCredit)
ReadModule('CS101')
#DeleteModule('CS101')
ReadModule('CS101')

# define module detail data
id = 1
module = 'CS101'
year = 2022
semester = 1
studentId = 2101447
gradePoint = 4.0

# Test for Module Detail
CreateModuleDetail(module, year, semester, studentId, gradePoint)
ReadModuleDetail(1)
grade_point = 3.5
UpdateModuleDetail(1, module, year, semester, studentId, gradePoint)
ReadModuleDetail(1)
#DeleteModuleDetail(1)
ReadModuleDetail(1)
