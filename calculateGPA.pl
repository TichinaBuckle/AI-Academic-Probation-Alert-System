% Knowledge base to store total credits and total grade points earned
:- dynamic(total_credits/1).
:- dynamic(total_gpe/1).

% Initialize total credits and total grade points
total_credits(0).
total_gpe(0).

% student(sid)
% course(sid, credits, grade_point)
student(2000322).
student(2000685).
student(2000146).
course(2000322, 4, 3.5).
course(2000322, 3, 3.0).
course(2000685, 4, 2.7).
course(2000685, 3, 3.2).
course(2000146, 4, 3.8).
course(2000146, 3, 3.9).

findStudents(X) :- findall(Student, student(Student), X).
findStudentsGrades(Sid) :- findall(Credits, course(Sid, Credits, '_'), X), write(X).


% Main func to get the credits and gp
calculate :- write('Enter the credits of the module'), read(Credits),
            nl, write('Enter the grade point earned: '), read(Grade_Point),
		calculate_gpe(Credits, Grade_Point, GPE),
            addCredits(Credits, Total_Credits),
            addGradePoints(GPE, Total_GPE),
            nl, write('Do you want to enter another module? (y/n)'), read(Choice),
            (Choice = 'y' -> calculate; calculate_gpa(Total_Credits, Total_GPE, GPA),
            nl, write('Your GPA is: '), write(GPA)).


% Calculate the total credits
addCredits(Credits, Total_Credits) :- retract(total_credits(Old_Credits)),
		Total_Credits is Old_Credits + Credits,
		assert(total_credits(Total_Credits)).

% Calculate the total GPE
addGradePoints(GPE, Total_GPE) :- retract(total_gpe(Old_GPE)),
		Total_GPE is Old_GPE + GPE,
		assert(total_gpe(Total_GPE)).

% Calculate the GPE
calculate_gpe(Credits, Grade_Point, GPE) :- GPE is Grade_Point * Credits.

%Calculate the GPA
calculate_gpa(Total_Credits, Total_GPE, GPA) :- GPA is Total_GPE / Total_Credits.
