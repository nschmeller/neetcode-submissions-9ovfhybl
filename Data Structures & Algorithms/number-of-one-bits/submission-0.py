class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        curr = 1
        while curr <= n:
            if n & curr != 0:
                count += 1
            curr <<= 1
        
        return count
