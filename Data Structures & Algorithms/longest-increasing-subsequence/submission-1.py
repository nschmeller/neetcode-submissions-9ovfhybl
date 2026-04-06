from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def subsequence(i):
            return 1+ max((subsequence(j) for j in range(i+1, len(nums)) if nums[i] < nums[j]), default=0)
        
        return max(subsequence(i) for i in range(len(nums)))
