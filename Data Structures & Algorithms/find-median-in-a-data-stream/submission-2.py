from heapq import heappush, heappop, heappush_max, heappop_max

class MedianFinder:

    def __init__(self):
        self.lower, self.upper = [], []
        

    def addNum(self, num: int) -> None:
        heappush_max(self.lower, num)
        heappush(self.upper, heappop_max(self.lower))

        if len(self.upper) > len(self.lower):
            heappush_max(self.lower, heappop(self.upper))
  

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return self.lower[0]
        else:
            return (self.lower[0] + self.upper[0]) / 2
