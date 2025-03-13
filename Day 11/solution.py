def next_greater_element(nums):
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        
        if stack:
            result[i] = stack[-1]
        
        stack.append(nums[i])
    
    return result

# Example usage:
print(next_greater_element([4, 5, 2, 10, 8]))  # Output: [5, 10, 10, -1, -1]
print(next_greater_element([3, 7, 1, 8, 2, 9]))  # Output: [7, 8, 8, 9, 9, -1]
