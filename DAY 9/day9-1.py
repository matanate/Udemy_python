studet_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Drako" : 74,
    "Neville" : 62
}

student_grades = {}

for key in studet_scores:
    if studet_scores[key] <= 70:
        student_grades[key] = "Fail"
    elif studet_scores[key] <= 80 and studet_scores[key] > 70:
        student_grades[key] = "Acceptable"
    elif studet_scores[key] <= 90 and studet_scores[key] > 80:
        student_grades[key] = "Exeeds expectations"
    elif studet_scores[key] > 90:
        student_grades[key] = "Outstanding"

print(student_grades)