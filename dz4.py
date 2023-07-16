"""Searching the minimum value."""
w, x, y, z = 100, 200, 40, 300

# Comparing variables to find the minimum value
if w <= x and w <= y and w <= z:
    print("'w' is the minimum value")
elif x <= y and x <= z:
    print("'x' is the minimum value")
elif y <= z:
    print("'y' is the minimum value")
else:
    print("'z' is the minimum value")
    