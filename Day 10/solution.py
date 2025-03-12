from collections import Counter

def first_unique_character(s: str) -> int:
    char_count = Counter(s)
    
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index
    
    return -1

# Example usage:
print(first_unique_character("leetcode"))  # Output: 0
print(first_unique_character("loveleetcode"))  # Output: 2
print(first_unique_character("aabb"))  # Output: -1

# Solution for finding intersection of two arrays
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

# Example usage:
print(intersection([1, 2, 2, 1], [2, 2]))  # Output: [2]
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [9, 4]

# Solution for Two Sum problem
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Example usage:
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(two_sum([3, 2, 4], 6))  # Output: [1, 2]
print(two_sum([3, 3], 6))  # Output: [0, 1]

# Solution for checking duplicates in an array
def contains_duplicate(nums):
    return len(nums) != len(set(nums))

# Example usage:
print(contains_duplicate([1,2,3,1]))  # Output: True
print(contains_duplicate([1,2,3,4]))  # Output: False
print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))  # Output: True

# Solution for finding maximum subarray sum
def max_subarray_sum(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example usage:
print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
print(max_subarray_sum([1]))  # Output: 1
print(max_subarray_sum([5,4,-1,7,8]))  # Output: 23
