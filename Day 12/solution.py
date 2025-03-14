def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:  # Start a new sequence
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)

    return longest

# Example usage:
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # Output: 9
print(longest_consecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))  # Output: 7