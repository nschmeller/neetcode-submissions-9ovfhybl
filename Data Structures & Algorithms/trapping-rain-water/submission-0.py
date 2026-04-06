class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ml, mr = height[l], height[r]
        amount = 0

        while l < r:
            if ml < mr:
                l += 1
                ml = max(ml, height[l])
                amount += ml - height[l]
            else:
                r -= 1
                mr = max(mr, height[r])
                amount += mr - height[r]
        
        return amount
