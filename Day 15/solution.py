def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

# Example usage:
print(majority_element([3, 2, 3]))  # Output: 3
print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
print(majority_element([1]))  # Output: 1
