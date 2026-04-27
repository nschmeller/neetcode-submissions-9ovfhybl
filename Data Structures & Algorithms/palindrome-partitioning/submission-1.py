class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrome(cand):
            l, r = 0, len(cand) - 1
            while l < r:
                if cand[l] != cand[r]:
                    return False
                l, r = l+1, r-1
            return True
        
        res, part = [], []
        def decision(i):
            if i == len(s):
                res.append(part[:])
            else:
                for j in range(i, len(s)):
                    if palindrome(s[i:j+1]):
                        part.append(s[i:j+1])
                        decision(j+1)
                        part.pop()
        
        decision(0)
        return res
