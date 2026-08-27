# ===== LISTS - Storing Multiple Values =====

# A list is like a container that holds many items
my_marks = [85, 92, 78, 95, 88]
my_subjects = ["Maths", "Python", "AI", "Statistics", "Physics"]
mixed = [19, "AI Engineer", True, 9.0]  # can store different types!

print("My marks:", my_marks)
print("My subjects:", my_subjects)

# ---- Accessing items (INDEXING) ----
# Remember: Python starts counting from 0!
print("\nFirst subject:", my_subjects[0])   # Maths
print("Third subject:", my_subjects[2])    # AI
print("Last subject:", my_subjects[-1])    # Physics (negative goes from end)

# ---- Useful List Operations ----
print("\nTotal subjects:", len(my_subjects))       # length
print("Highest mark:", max(my_marks))             # maximum
print("Lowest mark:", min(my_marks))              # minimum
print("Total marks:", sum(my_marks))              # sum
print("Average mark:", sum(my_marks)/len(my_marks)) # average

# ---- Adding and Removing ----
my_subjects.append("Deep Learning")   # add at end
print("\nAfter adding:", my_subjects)

my_subjects.remove("Physics")         # remove specific item
print("After removing:", my_subjects)

# ---- Slicing (VERY important in AI/ML) ----
print("\nFirst 3 subjects:", my_subjects[0:3])
print("Last 2 subjects:", my_subjects[-2:])

# YOUR TURN - Create a list of 5 of your favourite movies
my_movies = ["One Piece", "PK", "Student Of The Year", "3 Idiots", "YJHD"]
# Print the 2nd and 4th movie
print("\nSecond Movie:", my_movies[1])   # PK
print("Fourth Movie:", my_movies[3])     # 3 idiots
# Print total count of movies
print("\nTotal Movies:", len(my_movies))
# Add one more movie
my_movies.append("Obsession")
# Print the list again
print("\nAfter adding:", my_movies)