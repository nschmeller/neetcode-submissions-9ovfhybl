from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        longest = 0

        l = 0
        max_frequency = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            max_frequency = max(max_frequency, counts[s[r]])

            while (r-l+1) - max_frequency > k:
                counts[s[l]] -= 1
                l += 1
            
            longest = max(longest, r-l+1)
        
        return longest
