class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * len(nums)
        for i in range(1, len(nums)):
            prefixes[i] *= prefixes[i-1] * nums[i-1]

        suffixes = [1] * len(nums)
        for i in reversed(range(len(nums)-1)):
            suffixes[i] *= suffixes[i+1] * nums[i+1]
        
        # prefixes: [1  1  2 8]
        # suffixes: [48 24 6 1]

        # prefixes: [1 -1 0 0 0]
        # suffixes: [0  6 6 3 1 ]
        return [prefixes[i] * suffixes[i] for i in range(len(nums))]
