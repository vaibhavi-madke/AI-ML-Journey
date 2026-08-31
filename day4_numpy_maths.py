import numpy as np

# ===== MATHS ON ENTIRE ARRAYS AT ONCE =====
# No loops needed! NumPy does it all in one line!

scores = np.array([65, 80, 72, 91, 58, 84, 76, 68, 95, 73])

print("=== Basic Statistics ===")
print(f"Scores  : {scores}")
print(f"Sum     : {np.sum(scores)}")
print(f"Average : {np.mean(scores):.2f}")
print(f"Median  : {np.median(scores):.2f}")
print(f"Highest : {np.max(scores)}")
print(f"Lowest  : {np.min(scores)}")
print(f"Std Dev : {np.std(scores):.2f}")   # how spread out scores are
print(f"Variance: {np.var(scores):.2f}")

# ---- Arithmetic on whole array at once ----
print("\n=== Scaling Marks ===")
print("Original      :", scores)
print("Add 5 bonus   :", scores + 5)         # adds 5 to EVERY element
print("Multiply by 2 :", scores * 2)
print("Percentage/100:", scores / 100)
print("Squared       :", scores ** 2)

# ---- Two arrays together ----
maths   = np.array([80, 75, 90, 85, 70])
science = np.array([70, 85, 80, 90, 75])

print("\n=== Two Subjects ===")
print("Maths  :", maths)
print("Science:", science)
print("Total  :", maths + science)
print("Average:", (maths + science) / 2)
print("Diff   :", maths - science)

# ---- Sorting ----
jumbled = np.array([34, 91, 12, 67, 45, 88, 23, 76])
print("\n=== Sorting ===")
print("Original  :", jumbled)
print("Sorted    :", np.sort(jumbled))
print("Reversed  :", np.sort(jumbled)[::-1])
print("Who is 1st:", np.argmax(jumbled))    # index of highest value
print("Who is last:", np.argmin(jumbled))   # index of lowest value

# ---- Mathematical functions ----
angles = np.array([0, 30, 45, 60, 90])
rads   = np.deg2rad(angles)           # convert degrees to radians

print("\n=== Math Functions ===")
print("Angles:", angles)
print("Sin   :", np.round(np.sin(rads), 2))
print("Cos   :", np.round(np.cos(rads), 2))

numbers = np.array([1, 4, 9, 16, 25, 100])
print("\nNumbers    :", numbers)
print("Square root:", np.sqrt(numbers))
print("Log        :", np.round(np.log(numbers), 2))