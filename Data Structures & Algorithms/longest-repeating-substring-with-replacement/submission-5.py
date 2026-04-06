from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts, longest = defaultdict(int), 0

        l = r = maxf = 0
        while r < len(s):
            counts[s[r]] += 1
            maxf = max(maxf, counts[s[r]])
            r += 1

            while r - l - maxf > k:
                counts[s[l]] -= 1
                l += 1
            longest = max(longest, r - l)

        return longest
