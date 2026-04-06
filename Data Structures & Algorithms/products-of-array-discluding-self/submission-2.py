class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * len(nums)
        for i in range(1, len(nums)):
            prefixes[i] = prefixes[i-1] * nums[i-1]

        suffixes = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            suffixes[i] = suffixes[i+1] * nums[i+1]

        return [prefixes[i] * suffixes[i] for i in range(len(nums))]
