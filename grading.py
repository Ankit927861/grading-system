import csv

def calculate_grade(marks):
    marks = float(marks)

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"


def read_students(filename):
    students = []

    with open(filename, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["name"]
            marks = float(row["marks"])
            grade = calculate_grade(marks)

            students.append({
                "name": name,
                "marks": marks,
                "grade": grade
            })

    return students
