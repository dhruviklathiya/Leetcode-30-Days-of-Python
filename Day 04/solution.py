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
