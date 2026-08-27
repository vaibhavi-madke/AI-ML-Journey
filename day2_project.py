# ===== MINI PROJECT: Student Report Card Generator =====

def calculate_average(marks):
    return sum(marks) / len(marks)

def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"

def get_remark(average):
    if average >= 90:
        return "Outstanding! Future AI Engineer! "
    elif average >= 80:
        return "Excellent work! Keep pushing! "
    elif average >= 70:
        return "Good effort! Room to grow! "
    elif average >= 60:
        return "Average. You can do better! "
    else:
        return "Need serious improvement. Don't give up! "

def print_report(name, age, subjects, marks):
    avg = calculate_average(marks)
    grade = get_grade(avg)
    remark = get_remark(avg)

    print("\n" + "="*40)
    print("       STUDENT REPORT CARD")
    print("="*40)
    print(f"Name     : {name}")
    print(f"Age      : {age}")
    print("-"*40)
    print(f"{'Subject':<15} {'Marks':<10} {'Status'}")
    print("-"*40)
    for i in range(len(subjects)):
        status = "Pass " if marks[i] >= 60 else "Fail "
        print(f"{subjects[i]:<15} {marks[i]:<10} {status}")
    print("-"*40)
    print(f"Average  : {avg:.2f}")
    print(f"Grade    : {grade}")
    print(f"Remark   : {remark}")
    print("="*40)

# ----- MAIN PROGRAM -----
print("Welcome to Report Card Generator!")
name = input("Enter student name: ")
age = int(input("Enter age: "))

subjects = ["Maths", "Python", "AI Basics", "Statistics", "Physics"]
marks = []

print(f"\nEnter marks for {name} (out of 100):")
for subject in subjects:
    mark = int(input(f"  {subject}: "))
    marks.append(mark)

print_report(name, age, subjects, marks)