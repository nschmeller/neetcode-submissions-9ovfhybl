from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        present = set(nums)

        starts = set()
        for num in nums:
            if num-1 not in present:
                starts.add(num)
        
        longest = 0
        for start in starts:
            curr = start
            count = 0
            while True:
                if curr in present:
                    curr += 1
                    count += 1
                    longest = max(longest, count)
                else:
                    break
        
        return longest
