from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freqs = defaultdict(list)

        for num in counts:
            freqs[counts[num]].append(num)

        remaining = k
        res = []
        for i in reversed(range(len(nums)+1)):
            if freqs[i]:
                res += freqs[i]
                remaining -= len(freqs[i])
            if remaining == 0:
                return res
        return res
