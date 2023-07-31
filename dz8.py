"""Find max multiplication of three values in the list."""

nums = [-67, -90, -3, -2, -1, -5, -45, -32, -4]


def max_multip_of_three(nums):
    """
    Create a function to find the maximum multiplication
    of the three values in the list.
    """
    if len(nums) < 3:
        return 'Not enough numbers in the list'

    nums.sort()
    print(nums)
    
    max_product_1 = nums[-1] * nums[-2] * nums[-3]
    max_product_2 = nums[0] * nums[1] * nums[-1]

    if max_product_1 > max_product_2 and max_product_1 > 0:
        return f"Max value = \'{max_product_1}\'. " \
               f'Nums are: ({nums[-3]}, {nums[-2]}, {nums[-1]})'
    elif max_product_2 > max_product_1:
        return f"Max value = \'{max_product_2}\'. " \
               f'Nums are: ({nums[0]}, {nums[1]}, {nums[-1]})'
    elif max_product_1 < 0 and max_product_2 < 0:
        return 'All numbers in the list are negative'
    else:
        return 'Max integer zero'


print(max_multip_of_three(nums), end='\n\n')

#  Examples оf function usage
l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]
print(max_multip_of_three(l1), end='\n\n')
l2 = [-1, 1, 2, 0, 3, 12, 4, 5, -1, 6]
print(max_multip_of_three(l2), end='\n\n')
