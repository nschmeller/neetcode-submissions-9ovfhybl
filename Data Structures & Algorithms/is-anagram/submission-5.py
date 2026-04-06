from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freqs = defaultdict(int)
        for c in s:
            s_freqs[c] += 1
        
        t_freqs = defaultdict(int)
        for c in t:
            t_freqs[c] += 1
        
        return s_freqs == t_freqs
        