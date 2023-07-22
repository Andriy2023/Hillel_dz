"""Compiling a new list using comprehension."""

from itertools import zip_longest

# lists № 1
l1 = [1, 3, 5, 7]
l2 = [1, 4, 5]

# lists № 2
# l1 = [1, 4, 5]
# l2 = [1, 3, 5, 7]

# lists № 3
# l1 = [2, 4, 6, 8, 10]
# l2 = [1, 2, 3]

# Get the maximum length between the two lists
max_length = max(len(l1), len(l2))

# Using zip_longest to pair up elements and
# filling the missing elements digit 0
var1 = zip_longest(l1, l2, fillvalue=0)

# Create a dictionary with a default value of 0
result_dict = {i: (x, y) for i, (x, y) in enumerate(var1)}

# Create the list_target using a list comprehension,
# taking values from the dictionary result_dict
list_target = [(result_dict[i][0], result_dict[i][1])
               for i in range(max_length)]

print(list_target)
