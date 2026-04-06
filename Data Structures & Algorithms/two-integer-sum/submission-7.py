class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i, num in enumerate(nums):
            if num in diffs:
                return [min(diffs[num], i), max(diffs[num], i)]
            else:
                diffs[target - num] = i
