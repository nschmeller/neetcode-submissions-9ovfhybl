class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = set()
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k < len(nums):
                if nums[j] + nums[k] < -nums[i]:
                    j += 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
        
        return [[i, j, k] for i, j, k in res]
