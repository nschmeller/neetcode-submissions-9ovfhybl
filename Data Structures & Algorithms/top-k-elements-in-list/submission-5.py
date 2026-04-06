from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freqs = defaultdict(list)

        for num, count in counts.items():
            freqs[count].append(num)
        
        res = []
        print(freqs)
        for i in reversed(range(len(nums)+1)):
            res += freqs[i]
            print(res)
            if len(res) == k:
                return res
