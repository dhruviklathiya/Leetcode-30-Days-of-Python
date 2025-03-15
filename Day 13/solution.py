def first_missing_positive(nums):
    n = len(nums)

    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]  # Swap

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1

# Example usage:
print(first_missing_positive([1, 2, 0]))  # Output: 3
print(first_missing_positive([3, 4, -1, 1]))  # Output: 2
print(first_missing_positive([7, 8, 9, 11, 12]))  # Output: 1