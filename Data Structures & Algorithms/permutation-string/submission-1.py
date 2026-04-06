from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm, counts = Counter(s1), Counter(s2[:len(s1) - 1])

        l, r = 0, len(s1) - 1
        for l, r in zip(range(len(s2)), range(len(s1) - 1, len(s2))):
            counts[s2[r]] += 1

            if perm == counts:
                return True
            else:
                counts[s2[l]] -= 1

            l += 1
            r += 1
        
        return False
                