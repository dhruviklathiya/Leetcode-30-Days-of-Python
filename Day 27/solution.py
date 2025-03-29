from collections import Counter

def find_anagrams(s: str, p: str):
    res = []
    p_count = Counter(p)
    s_count = Counter()

    for i in range(len(s)):
        s_count[s[i]] += 1

        # Remove char left of the window
        if i >= len(p):
            if s_count[s[i - len(p)]] == 1:
                del s_count[s[i - len(p)]]
            else:
                s_count[s[i - len(p)]] -= 1

        # Compare window with pattern
        if s_count == p_count:
            res.append(i - len(p) + 1)

    return res

# Example usage:
print(find_anagrams("cbaebabacd", "abc"))  # Output: [0, 6]
print(find_anagrams("abab", "ab"))         # Output: [0, 1, 2]
