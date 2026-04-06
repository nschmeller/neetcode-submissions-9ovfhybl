class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def find(num, start):
            l, r = start, len(numbers) - 1
            while l <= r:
                mid = (l + r) // 2
                print(l, r, num, start)
                if numbers[mid] < num:
                    l = mid + 1
                elif numbers[mid] > num:
                    r = mid - 1
                else:
                    return mid

            return -1
        
        for i, num in enumerate(numbers):
            if target - num == num:
                continue
            pair = find(target - num, i+1)
            if pair != -1:
                return [i+1, pair+1]
