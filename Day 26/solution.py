from collections import Counter
import heapq

def top_k_frequent(nums, k):
    count = Counter(nums)
    return [item for item, freq in heapq.nlargest(k, count.items(), key=lambda x: x[1])]

# Example usage:
print(top_k_frequent([1,1,1,2,2,3], 2))  # Output: [1, 2]
print(top_k_frequent([1], 1))           # Output: [1]
