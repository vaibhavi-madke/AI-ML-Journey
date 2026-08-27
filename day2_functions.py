# ===== FUNCTIONS - Reusable blocks of code =====
# Think of a function like a MACHINE
# You give it INPUT → it does work → gives you OUTPUT

# ---- Basic Function ----
def greet():
    print("Hello! Welcome to AI/ML Journey!")

greet()   # calling the function
greet()   # call it again - runs again!

# ---- Function with Parameters (inputs) ----
def greet_person(name, age):
    print(f"Hello {name}! You are {age} years old.")
    print(f"You have {25 - age} years to become an AI expert!")

greet_person("Arnav", 19)
greet_person("Sumedh", 20)

# ---- Function that RETURNS a value ----
def calculate_average(marks_list):
    total = sum(marks_list)
    average = total / len(marks_list)
    return average   # sends value back

my_marks = [85, 92, 78, 95, 88]
avg = calculate_average(my_marks)
print(f"\nYour average marks: {avg}")

# ---- Function with if/else inside ----
def get_grade(marks):
    if marks >= 90:
        return "A+ "
    elif marks >= 80:
        return "A "
    elif marks >= 70:
        return "B "
    elif marks >= 60:
        return "C "
    else:
        return "F - Study Harder "

# Test it with different marks
test_marks = [95, 83, 71, 65, 45]
print("\n=== Grade Card ===")
for mark in test_marks:
    grade = get_grade(mark)
    print(f"Marks: {mark} -> Grade: {grade}")

# ---- YOUR TURN ----
# Write a function called 'is_even_or_odd'
# It takes a number as input
# Returns "Even" if number is even, "Odd" if odd
# Test it with numbers 1 to 10 using a loop

def is_even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test with numbers 1 to 10
print("Check Even Odd")
for i in range(1, 11):
    result = is_even_or_odd(i)
    print(f"{i} is {result}")