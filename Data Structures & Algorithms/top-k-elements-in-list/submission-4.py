from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freqs = defaultdict(list)

        for num in counts:
            freqs[counts[num]].append(num)
        
        curr = len(nums)
        remaining = k
        res = []
        while remaining > 0 and curr >= 0:
            res += freqs[curr]
            remaining -= len(freqs[curr])
            curr -= 1
        return res