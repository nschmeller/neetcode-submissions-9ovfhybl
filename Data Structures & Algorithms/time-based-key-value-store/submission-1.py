from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.store[key]) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if timestamp >= self.store[key][mid][0]:
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return self.store[key][res][1] if res != -1 else ""
