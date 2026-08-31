import numpy as np   # 'np' is the standard shortcut everyone uses

# ===== CREATING ARRAYS =====

# From a list
marks = np.array([85, 92, 78, 95, 88, 76, 91])
print("Array:", marks)
print("Type:", type(marks))
print("Data type:", marks.dtype)     # int64
print("Shape:", marks.shape)         # (7,) = 7 items, 1 row

# ---- Special Arrays ----
zeros   = np.zeros(5)               # [0. 0. 0. 0. 0.]
ones    = np.ones(5)                # [1. 1. 1. 1. 1.]
rng     = np.arange(0, 10, 2)      # [0 2 4 6 8] like range()
lins   = np.linspace(0, 1, 5)     # [0, 0.25, 0.5, 0.75, 1.0]

print("\nZeros :", zeros)
print("Ones  :", ones)
print("Range :", rng)
print("Linear:", lins)

# ---- Random Arrays (used CONSTANTLY in AI/ML) ----
np.random.seed(42)                          # seed = same random every time
rand_int   = np.random.randint(0, 100, 8)  # 8 random ints between 0-100
rand_float = np.random.random(5)            # 5 random floats 0 to 1

print("\nRandom ints  :", rand_int)
print("Random floats:", rand_float)

# ===== INDEXING & SLICING (same logic as lists but more powerful) =====
scores = np.array([45, 78, 92, 61, 88, 35, 74, 95, 52, 83])

print("\n=== Indexing ===")
print("First :", scores[0])
print("Last  :", scores[-1])
print("3rd   :", scores[2])

print("\n=== Slicing ===")
print("First 5      :", scores[:5])
print("Last 3       :", scores[-3:])
print("Middle (3-7) :", scores[3:7])
print("Every 2nd    :", scores[::2])
print("Reversed     :", scores[::-1])

# ===== BOOLEAN INDEXING (SUPER powerful - used in data filtering) =====
print("\n=== Filtering with Conditions ===")
passed = scores[scores >= 60]          # only scores above 60
failed = scores[scores < 60]           # only scores below 60
high   = scores[scores >= 80]          # distinction

print("All scores  :", scores)
print("Passed (60+):", passed)
print("Failed (<60):", failed)
print("High (80+)  :", high)
print("Pass count  :", len(passed))
print("Fail count  :", len(failed))