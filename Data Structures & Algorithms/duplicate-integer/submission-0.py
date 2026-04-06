class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        items = {}

        for num in nums:
            if num in items:
                return True
            else:
                items[num] = True
        
        return False
