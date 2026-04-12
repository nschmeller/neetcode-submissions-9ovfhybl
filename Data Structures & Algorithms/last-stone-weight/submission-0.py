from heapq import heapify_max, heappush_max, heappop_max

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapify_max(heap)

        while len(heap) > 1:
            first, second = heappop_max(heap), heappop_max(heap)
            if abs(first - second) > 0:
                heappush_max(heap, abs(first - second))
        
        if heap:
            return heap[0]
        else:
            return 0
