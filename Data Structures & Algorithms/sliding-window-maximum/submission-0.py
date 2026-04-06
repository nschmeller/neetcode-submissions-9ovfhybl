from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window, res = deque(), []
        
        l = r = 0
        while r < len(nums):
            while window and nums[window[-1]] < nums[r]:
                window.pop()
            window.append(r)
            r += 1

            if l > window[0]:
                window.popleft()
            
            if r >= k:
                res.append(nums[window[0]])
                l += 1
        
        return res
