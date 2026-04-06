class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        pivot = l

        def binary_search(l, r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        res = binary_search(0, pivot-1)
        if res != -1:
            return res
        else:
            return binary_search(pivot, len(nums)-1)
