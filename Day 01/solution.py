def longestConsecutive(nums):
    if not nums:
        return 0

    nums.sort()  # O(n log n)
    longest = 1
    current_length = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            current_length += 1
        elif nums[i] != nums[i - 1]:  # Handle duplicates
            current_length = 1

        longest = max(longest, current_length)

    return longest
