def single_number(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR operation
    return result

# Example usage:
print(single_number([2, 2, 1]))  # Output: 1
print(single_number([4, 1, 2, 1, 2]))  # Output: 4
print(single_number([1]))  # Output: 1
