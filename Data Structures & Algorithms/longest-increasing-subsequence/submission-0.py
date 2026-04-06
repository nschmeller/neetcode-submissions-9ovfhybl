from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def subsequence(curr, prev):
            if curr >= len(nums):
                return 0
            elif prev == -1 or nums[curr] > nums[prev]:
                return max(1 + subsequence(curr+1, curr), subsequence(curr+1, prev))
            else:
                return subsequence(curr+1, prev)
        
        return subsequence(0, -1)
