idef calculate_grade(marks):
    

    marks = float(marks)

    if marks < 0 or marks > 100:
        raise ValueError("Invalid marks")

    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"


def generate_report(filename):
    students = read_students(filename)

    for student in students:
        print(
            f"{student['name']}: "
            f"{student['marks']} - "
            f"{student['grade']}"
        )
