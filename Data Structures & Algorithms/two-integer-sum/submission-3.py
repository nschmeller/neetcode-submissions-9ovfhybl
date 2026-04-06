class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for i, num in enumerate(nums):
            diffs[target - num] = i
        
        for i, num in enumerate(nums):
            if num in diffs and diffs[num] != i:
                return [min(i, diffs[num]), max(i, diffs[num])]
