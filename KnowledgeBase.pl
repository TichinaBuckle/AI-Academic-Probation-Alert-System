% Group Members: - Tichina Buckle, Micah Brown, Ramoune Roberts, Winston
% Date Last Updated: 04-22-2024
% File Name: KnowledgeBase.pl
% Description: Contains Knowledge base for gpa

% Dynamic predicates
:- dynamic(total_credits/1).
:- dynamic(total_gpe/1).

% Facts
% student_master(StudentId, Name, Email, School, Programme)
% student_master(2000345, 'Winston', 'winstonmcleod@gmail.com',
% scit, comsci).

% module_master(Module, NumCredits)
% module_master('Artificial Intelligence', 4).

% module_details(Module, Year, Semester, StudentID, GradePoints)
% module_details('Artificial Intelligence', 2023, 2000345, 4, 3.67).


% Initialize total credits and total grade points
sem1TotalCredits(0).
sem1TotalGPE(0).

% Main function to get the credits and grade points
calculate :- write('Enter the credits of the module: '), read(Credits),
            nl, write('Enter the grade point earned: '), read(GradePoint),
            calculateGPE(Credits, GradePoint, GPE),
            addCredits(Credits, TotalCredits),
            addGradePoints(GPE, TotalGPE),
            nl, write('Do you want to enter another module? (y/n)'), read(Choice),
            (Choice = 'y' -> calculate; calculateGPA(TotalCredits, TotalGPE, GPA),
            nl, write('Your GPA is: '), write(GPA)).

% Calculations

% Total Credits for the modules taken by the student taken in each semester
sem1TotalCredits(StudentId, Year, Sem1Cred, Sem2Cred):-
    findall(Credit, moduleDetails(StudentId, Year, 1, Credit), CreditList1),
    sumList(CreditList1, Sem1Cred),   %Sem1
    findall(Credit, moduleDetails(StudentId, Year, 2, Credit), CreditList2),
    sumList(CreditList2, Sem2Cred).   %Sem2

sumList([], 0).
sumList([H|T], N):- sumList(T, N2), N is H + N2.

moduleDetails(StudentId, Year, Sem, Credit):-
    moduleDetails(StudentId, Module, Year, Sem, _),
    moduleMaster(Module, Credit).

% Multiply the GP for each module by the corresponding credits to get the [GP earned] for each module
gpEarned(StudentId, Year, Sem, GPE):-
    moduleDetails(StudentId, X, Year, Sem, GP),
    moduleMaster(X, Credit),
    GPE is GP * Credit.

% Calculate Total [GP earned] for each semester
totalGPEPerSem(StudentId, Year, Sem1Gp, Sem2Gp):-
    findall(GPE1, gpEarned(StudentId, Year, 1, GPE1), GPE1List),
    sumList(GPE1List, Sem1Gp),       %Sem1
    findall(GPE2, gpEarned(StudentId, Year, 2, GPE2), GPE2List),
    sumList(GPE2List, Sem2Gp).       %Sem2

% Divide Total [GP earned] by the Total Credits for the module taken in each semester
totalGPE(Year, TotalGpeSem1, TotalGpeSem2, StudentId):-
    totalGPEPerSem(StudentId, Year, Sem1Gp, Sem2Gp),
    sem1TotalCredits(StudentId, Year, Sem1Cred, Sem2Cred),
    TotalGpeSem1 is Sem1Gp / Sem1Cred,
    (Sem2Cred =:= 0 -> TotalGpeSem2 is 0; TotalGpeSem2 is Sem2Gp / Sem2Cred).

% If there is a semester 2, calculate the [cumulative gpa] by
% dividing the sum of Total [GP earned] for both semesters by the sum of [Total Credits] for both semesters
% If only semester one data is available then the [cumulative gpa] is the GPA for semester one
cumulativeGPA(Year, CumGPA, StudentId):-
    totalGPEPerSem(StudentId, Year, Sem1Gp, Sem2Gp),
    sem1TotalCredits(StudentId, Year, Sem1Cred, Sem2Cred),
    TotalGpeSem is Sem1Gp + Sem2Gp,
    TotalCredit is Sem1Cred + Sem2Cred,
    CumGPA is TotalGpeSem / TotalCredit.

% Get students' information including GPA
getStudents(Year, Id, Name, TotalGpeSem1, TotalGpeSem2, CGPA):-
    studentMaster(Id, Name, _, _, _),
    totalGPE(Year, TotalGpeSem1, TotalGpeSem2, Id),
    cumulativeGPA(Year, CGPA, Id),!.