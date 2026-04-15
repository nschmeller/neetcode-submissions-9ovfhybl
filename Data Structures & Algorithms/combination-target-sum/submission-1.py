class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        comb, res = [], []

        def backtrack(i, total):
            if i >= len(nums) or total > target:
                return
            elif total == target:
                res.append(list(comb))
            else:
                comb.append(nums[i])
                backtrack(i, total + nums[i])
                comb.pop()
                backtrack(i+1, total)
        
        backtrack(0, 0)
        return res
