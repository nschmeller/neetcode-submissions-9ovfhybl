from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freqs, t_freqs = defaultdict(int), defaultdict(int)

        for c in s:
            s_freqs[c] += 1
        for c in t:
            t_freqs[c] += 1
        
        return s_freqs == t_freqs
        