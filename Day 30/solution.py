def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Example usage:
print(missing_number([3, 0, 1]))           # Output: 2
print(missing_number([0, 1]))              # Output: 2
print(missing_number([9,6,4,2,3,5,7,0,1])) # Output: 8
