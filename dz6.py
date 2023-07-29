"""Compiling a new list using comprehension."""

# lists № 1
# l1 = [2, 4, 6, 8, 10]
# l2 = [1, 2, 3]

# lists № 2
l1 = [1, 3, 5, 7]
l2 = [1, 4, 5]

# lists № 3
# l1 = [1, 4, 5]
# l2 = [1, 3, 5, 7]

# Finding common indexes from both lists
index_l1 = set(range(len(l1)))
index_l2 = set(range(len(l2)))
index_union = index_l1.union(index_l2)


# Creating a dictionary of values
result_dict = {i: (l1[i] if i < len(l1) else 0,
                   l2[i] if i < len(l2) else 0)
               for i in index_union}


# Create the list_target using a list comprehension,
# taking values from the dictionary
list_target = [(result_dict[i][0], result_dict[i][1])
               for i in range(len(index_union))]

print(list_target)
