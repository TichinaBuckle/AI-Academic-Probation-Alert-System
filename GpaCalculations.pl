% Group Members: - Tichina Buckle, Micah Brown, Ramoune Roberts, Winston
% Date Last Updated: 04-22-2024
% File Name: GpaCalculations.pl
% Description: Contains calculations for gpa

% Dynamic predicates
:- dynamic(module_details/5).
:- dynamic(student/6).
:- dynamic(module/2).
:- dynamic(default_gpa/1).

%Assert a default GPA value
:-assert(default_gpa(2.2)).

sem1TotalCredits(0).
sem2TotalCredits(0).
sem1TotalGPE(0).
sem2TotalGPE(0).
cumulativeGPA(0).

% student(id, fname, lname, email, school, programme).
% module(code, credits)
% module_details(module, year, semester, student_ID, grade_points)

% Main Function
calculate([], []).

% Enter a single student ID to retrieve their GPA
calculate(Year, Sid, GPA) :-
    calculateSem1(Year, Sid, Sem1TotalCredits, Sem1TotalGPE),
    calculateSem2(Year, Sid, Sem2TotalCredits, Sem2TotalGPE),
    calculateCumulativeGPA(Sem1TotalCredits, Sem2TotalCredits, Sem1TotalGPE, Sem2TotalGPE, GPA).

% Calculate Semester 1 GPA
calculateSem1(Year, Sid, Sem1TotalCredits, Sem1TotalGPE) :-
    Semester is 1,
    totalCredits(Sid, Year, Semester, Sem1TotalCredits), % Gets the total credits for the student,
    totalGPE(Sid, Year, Semester, Sem1TotalGPE). % Gets the total grade points earned for the student

% Calculate Semester 2 GPA
calculateSem2(Year, Sid, Sem2TotalCredits, Sem2TotalGPE) :-
    Semester is 2,
    totalCredits(Sid, Year, Semester, Sem2TotalCredits), % Gets the total credits for the student,
    totalGPE(Sid, Year, Semester, Sem2TotalGPE). % Gets the total grade points earned for the student

% Calculate total credits
totalCredits(Sid, Year, Semester, TotalCredits) :-
    studentsModules(Sid, Year, Semester, Modules),
    sumCredits(Modules, TotalCredits).

% Calculate total grade points earned
totalGPE(Sid, Year, Semester, TotalGPE) :-
    studentsModuleAndGradePoint(Sid, Year, Semester, AllModuleGradePoints),
    sumGradePoints(AllModuleGradePoints, TotalGPE).

% Get the list of course credits for a student
studentsModules(Sid, Year, Semester, Modules) :-
    % module_details(module, year, semester, student_ID, grade_points)
    findall(Module, moduleDetails(Module, Year, Semester, Sid, _), Modules).

% Get the list of course credits and grade points for a student
studentsModuleAndGradePoint(Sid, Year, Semester, AllModuleGradePoints) :-
    % module_details(module, year, semester, student_ID, grade_points)
    findall([Module, Grade_Point], moduleDetails(Module, Year, Semester, Sid, Grade_Point), AllModuleGradePoints).

% Calculate the total credits
sumCredits([], 0).  % Base case: Sum of an empty list is 0
sumCredits([Module | MTail], TotalCredits) :-
    module(Module, Credit),  % Get the credit for the module
    sumCredits(MTail, RemainingCredits),  % Recursively sum the tail of the list
    TotalCredits is Credit + RemainingCredits.  % Calculate total credits

% Calculate the total grade points earned
sumGradePoints([], 0).  % Base case: Sum of an empty list is 0
sumGradePoints([[Module, Grade_Point] | Tail], TotalGPE) :-
    module(Module, Credit),  % Get the credit for the module
    sumGradePoints(Tail, Remaining),
    GPE is Credit * Grade_Point,
    TotalGPE is GPE + Remaining.

% Calculate the GPA
calculateGPA(TotalCredits, TotalGPE, GPA) :- GPA is TotalGPE / TotalCredits.

% Calculate the Cumulative GPA
calculateCumulativeGPA(Sem1TotalCredits, Sem2TotalCredits, Sem1TotalGPE, Sem2TotalGPE, CumulativeGPA) :-
    TotalCredits is Sem1TotalCredits + Sem2TotalCredits,
    TotalGPE is Sem1TotalGPE + Sem2TotalGPE,
    TotalCredits > 0,
    CumulativeGPA is TotalGPE / TotalCredits,
    !.
calculateCumulativeGPA(_, _, _, _, 0.0).
