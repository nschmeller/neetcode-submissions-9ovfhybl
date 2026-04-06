from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def climb(step):
            if step == n:
                return 1
            elif step >= n:
                return 0
            else:
                return climb(step+1) + climb(step+2)

        return climb(0)
