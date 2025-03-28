def move_zeroes(nums):
    insert_pos = 0
    
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1

# Example usage:
nums1 = [0, 1, 0, 3, 12]
move_zeroes(nums1)
print(nums1)  # Output: [1, 3, 12, 0, 0]

nums2 = [0]
move_zeroes(nums2)
print(nums2)  # Output: [0]
