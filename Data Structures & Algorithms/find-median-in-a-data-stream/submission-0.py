from heapq import heappush, heappop, heappush_max, heappop_max

class MedianFinder:

    def __init__(self):
        self.lower, self.upper = [], []
    

    def addNum(self, num: int) -> None:
        if self.upper and num > self.upper[0]:
            heappush(self.upper, num)
        else:
            heappush_max(self.lower, num)
        
        if len(self.lower) > len(self.upper) + 1:
            heappush(self.upper, heappop_max(self.lower))
        if len(self.upper) > len(self.lower) + 1:
            heappush_max(self.lower, heappop(self.upper))
        

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return self.lower[0]
        elif len(self.lower) < len(self.upper):
            return self.upper[0]
        else:
            return (self.lower[0] + self.upper[0]) / 2
