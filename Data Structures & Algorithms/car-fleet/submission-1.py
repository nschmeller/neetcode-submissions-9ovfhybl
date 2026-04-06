class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []

        for time in ((target - pos) / sp for pos, sp in sorted(zip(position, speed), reverse=True)):
            if not fleets or fleets[-1] < time:
                fleets.append(time)
        
        return len(fleets)
