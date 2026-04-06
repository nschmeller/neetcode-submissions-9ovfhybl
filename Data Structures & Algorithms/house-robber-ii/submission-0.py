class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        one_back_first = two_back_first = 0
        for num in nums[:-1]:
            one_back_first, two_back_first = max(num + two_back_first, one_back_first), one_back_first
        
        one_back_second = two_back_second = 0
        for num in nums[1:]:
            one_back_second, two_back_second = max(num + two_back_second, one_back_second), one_back_second

        return max(one_back_first, one_back_second)
