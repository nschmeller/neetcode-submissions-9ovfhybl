from collections import Counter, deque
from heapq import heapify_max, heappush_max, heappop_max

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = list(Counter(tasks).values())
        heapify_max(heap)
        cooldown, res = deque(), 0

        while heap or cooldown:
            res += 1

            if heap:
                remaining = heappop_max(heap) - 1
                if remaining > 0:
                    cooldown.append((res + n, remaining))

            if cooldown and cooldown[0][0] == res:
                heappush_max(heap, cooldown.popleft()[1])

        return res
