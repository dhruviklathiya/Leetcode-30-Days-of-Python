def subarraySum(nums, k):
    prefix_sum_map = {0: 1}  # To handle cases where subarray starts from index 0
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num  # Update running sum

        # Check if (current_sum - k) exists in the map
        if (current_sum - k) in prefix_sum_map:
            count += prefix_sum_map[current_sum - k]

        # Update prefix_sum_map with current_sum frequency
        prefix_sum_map[current_sum] = prefix_sum_map.get(current_sum, 0) + 1

    return count
