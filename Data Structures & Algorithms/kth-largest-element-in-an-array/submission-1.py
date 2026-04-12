from random import randint

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Lomuto partitioning
        def quickselect(lo, hi, k):
            while lo < hi:
                pivot = randint(lo, hi)
                nums[pivot], nums[hi] = nums[hi], nums[pivot]

                store = lo
                for i in range(lo, hi):
                    if nums[i] < nums[hi]:
                        nums[store], nums[i] = nums[i], nums[store]
                        store += 1
                nums[store], nums[hi] = nums[hi], nums[store]

                if store == k:
                    return nums[k]
                elif store < k:
                    lo = store + 1
                else:
                    hi = store - 1
            
            return nums[lo]
        
        return quickselect(0, len(nums) - 1, len(nums) - k)
