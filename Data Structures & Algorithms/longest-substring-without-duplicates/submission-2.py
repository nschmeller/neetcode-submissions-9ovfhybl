from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr, longest = defaultdict(int), 0
        l = r = 0

        while r < len(s):
            while curr[s[r]] > 0:
                curr[s[l]] -= 1
                l += 1
            else:
                curr[s[r]] += 1
                r += 1
            longest = max(longest, r - l)
        
        return longest
