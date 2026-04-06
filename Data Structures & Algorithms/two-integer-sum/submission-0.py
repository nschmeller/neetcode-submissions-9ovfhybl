class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        deltas = {}

        for i in range(len(nums)):
            delta = target - nums[i]
            if delta in deltas:
                return [min(i, deltas[delta]), max(i, deltas[delta])]
            else:
                deltas[nums[i]] = i
