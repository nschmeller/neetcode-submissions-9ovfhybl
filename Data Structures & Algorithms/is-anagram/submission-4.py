class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        for c in s:
            if c in s_freq:
                s_freq[c] += 1
            else:
                s_freq[c] = 0
        
        t_freq = {}
        for c in t:
            if c in t_freq:
                t_freq[c] += 1
            else:
                t_freq[c] = 0
        
        return s_freq == t_freq
