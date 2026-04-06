class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = nums[0]
        prefix = suffix = 0

        for i in range(len(nums)):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[len(nums) - i - 1] * (suffix or 1)
            global_max = max(global_max, prefix, suffix)
        
        return global_max
