class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        start = l
        tr = lambda x: (x + start) % len(nums)

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[tr(mid)]:
                l = mid + 1
            elif target < nums[tr(mid)]:
                r = mid - 1
            else:
                return tr(mid)
        
        return -1
