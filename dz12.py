"""Counting the sum of the elements of a list."""


def recursive_sum(target_list):
    # check if target_list belongs to the list
    if not isinstance(target_list, list):
        return target_list
    else:
        # elements of the list recursively accessing each element of the list
        return sum(recursive_sum(numb) for numb in target_list)


# list for test
input_list = [[[[1, 4, 5], [[6, 9], [[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]
result = recursive_sum(input_list)


print('Target sum  =', result)
