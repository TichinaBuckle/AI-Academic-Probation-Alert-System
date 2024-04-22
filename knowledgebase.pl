% Dynamic predicates
:- dynamic(module_details/5).
:- dynamic(student_master/5).
:- dynamic(module_master/2).
:- dynamic(default_gpa/1).
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

% Assert a default GPA value
:- assert(default_gpa(2.2)).

% Initialize total credits and total grade points
totalCredits(0).
totalGpe(0).

% Main func to get the credits and gp
calculate :- write('Enter the credits of the module: '), read(Credits),
            nl, write('Enter the grade point earned: '), read(Grade_Point),
            calculate_gpe(Credits, Grade_Point, GPE),
            addCredits(Credits, Total_Credits),
            addGradePoints(GPE, Total_GPE),
            nl, write('Do you want to enter another module? (y/n)'), read(Choice),
            (Choice = 'y' -> calculate; calculate_gpa(Total_Credits, Total_GPE, GPA),
            nl, write('Your GPA is: '), write(GPA)).


% Calculations

% Total Credits for the modules taken by the student taken in each semester
totalCredits(StudentId, Year, Sem1_Cred, Sem2_Cred):-
    findall(Credit, moddet(StudentId, Year, 1, Credit), CreditList1),
    sum_list(CreditList1, Sem1_Cred),   %Sem1
    findall(Credit, moddet(StudentId, Year, 2, Credit), CreditList2),
    sum_list(CreditList2, Sem2_Cred).   %Sem2

sum_list([], 0).
sum_list([H|T], N):- sum_list(T, N2), N is H + N2.

moddet(StudentId, Year, Sem, Credit):-
    module_details(StudentId, Module, Year, Sem, _),
    module_master(Module, Credit).

% Multiply the GP for each module by the corresponding credits to get the [GP earned] for each module
gp_earned(StudentId, Year, Sem, GPE):-
    module_details(StudentId, X, Year, Sem, GP),
    module_master(X, Credit),
    GPE is GP * Credit.

% Calculate Total [GP earned] for each semester
total_gpe_per_sem(StudentId, Year, Sem1Gp, Sem2Gp):-
    findall(GPE1, gp_earned(StudentId, Year, 1, GPE1), GPE1_List),
    sum_list(GPE1_List, Sem1Gp),       %Sem1
    findall(GPE2, gp_earned(StudentId, Year, 2, GPE2), GPE2_List),
    sum_list(GPE2_List, Sem2Gp).       %Sem2

% Divide Total [GP earned] by the Total Credits for the module taken in each semester
total_gpe(Year, Total_gpe_sem1, Total_gpe_sem2, StudentId):-
    total_gpe_per_sem(StudentId, Year, Sem1Gp, Sem2Gp),
    totalCredits(StudentId, Year, Sem1_Cred, Sem2_Cred),
    Total_gpe_sem1 is Sem1Gp / Sem1_Cred,
    (Sem2_Cred =:= 0 -> Total_gpe_sem2 is 0; Total_gpe_sem2 is Sem2Gp / Sem2_Cred).

% If there is a semester 2, calculate the [cumulative gpa] by
% dividing the sum of Total [GP earned] for both semesters by the sum of [Total Credits] for both semesters
% If only semester one data is available then the [cumulative gpa] is the GPA for semester one
cumulative_gpa(Year, Cum_GPA, StudentId):-
    total_gpe_per_sem(StudentId, Year, Sem1Gp, Sem2Gp),
    totalCredits(StudentId, Year, Sem1_Cred, Sem2_Cred),
    Total_gpe_sem is Sem1Gp + Sem2Gp,
    Total_credit is Sem1_Cred + Sem2_Cred,
    Cum_GPA is Total_gpe_sem / Total_credit.

% Get students' information including GPA
get_students(Year, Id, Name, Total_gpe_sem1, Total_gpe_sem2, CGPA):-
    student_master(Id, Name, _, _, _),
    total_gpe(Year, Total_gpe_sem1, Total_gpe_sem2, Id),
    cumulative_gpa(Year, CGPA, Id),!.
    % nl, write(Id), write(Name), tab(2), write(Total_gpe_sem1), tab(2), write(Total_gpe_sem2), tab(2), write(CGPA),!.
