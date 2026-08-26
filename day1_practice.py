#1.Variables
name = "Vaibhav"        # String (text)
age = 19              # Integer (whole number)
percentage = 87.5     # Float (decimal number)
is_student = True     # Boolean (True/False)

print(type(name))       # tells you what TYPE it is
print(type(age))
print(type(percentage))
print(type(is_student))

#2.Taking Input From User
your_name = input("Enter your name: ")
your_age = input("Enter your age: ")
print("Hello", your_name, "! You are", your_age, "years old.")

#3. Basic Maths In Python
a = 15
b = 4
print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a // b)   # Floor division (removes decimal)
print(a % b)    # Modulus (remainder)
print(a ** b)   # Power (15 to the power 4)

#4. If/Else(Decision Making)
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Outstanding!")
elif marks >= 75:
    print("Very Good! Keep going!")
elif marks >= 60:
    print("Good. Push harder.")
else:
    print("Don't give up. Start again tomorrow.")

#5. print("Counting my journey days:")
for day in range(1, 11):
    print("Day", day, "- I showed up.")
    