"""
nums[k] = -nums[i] - nums[j]
nums[k] + nums[j] = -nums[i]
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        triples = []

        for i, num in enumerate(sorted_nums[:len(nums)-2]):
            if num > 0:
                break # sorted list means we can't find any more negatives
            if i > 0 and num == sorted_nums[i-1]:
                continue # do not attempt duplicate

            j, k = i+1, len(nums)-1
            while j < k:
                if sorted_nums[j] + sorted_nums[k] < -num:
                    j += 1
                elif sorted_nums[j] + sorted_nums[k] > -num:
                    k -= 1
                else:
                    triples.append([num, sorted_nums[j], sorted_nums[k]])
                    j += 1
                    k -= 1
                    while sorted_nums[j] == sorted_nums[j-1] and j < k:
                        j += 1
        
        return triples
