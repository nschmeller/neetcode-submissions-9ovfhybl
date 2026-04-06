class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def dfs(idx):
            if sum(comb) == target:
                res.append(comb[:])
            if sum(comb) >= target or idx >= len(nums):
                return
            comb.append(nums[idx])
            dfs(idx)
            comb.pop()
            dfs(idx+1)
        
        dfs(0)
        return res
