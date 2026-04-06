class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[len(nums)-1] = True

        for i in range(len(nums)-2, -1, -1):
            for j in range(nums[i]+1):
                if i + j < len(nums):
                    dp[i] |= dp[i+j]
        
        return dp[0]
