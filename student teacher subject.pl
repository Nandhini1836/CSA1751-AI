teaches(ram, ai).
teaches(sita, os).

studies(arun, ai).
studies(meena, os).

student_teacher(Student, Teacher) :-
    studies(Student, Subject),
    teaches(Teacher, Subject).
