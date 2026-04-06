class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i, num in enumerate(nums):
            if num in diffs:
                return [min(i, diffs[num]), max(i, diffs[num])]
            else:
                diffs[target - num] = i
