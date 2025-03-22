def move_zeroes(nums):
    non_zero_pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]
            non_zero_pos += 1

# Example usage:
arr1 = [0, 1, 0, 3, 12]
move_zeroes(arr1)
print(arr1)  # Output: [1, 3, 12, 0, 0]

arr2 = [0, 0, 1]
move_zeroes(arr2)
print(arr2)  # Output: [1, 0, 0]
