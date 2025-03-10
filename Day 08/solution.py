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
