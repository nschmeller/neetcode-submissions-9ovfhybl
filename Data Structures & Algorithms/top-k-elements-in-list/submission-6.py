from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freqs = defaultdict(list)
        for num in counts:
            freqs[counts[num]].append(num)
        
        res, remaining = [], k
        for i in range(len(nums), -1, -1):
            res += freqs[i]
            remaining -= len(freqs[i])
            if remaining <= 0:
                return res
