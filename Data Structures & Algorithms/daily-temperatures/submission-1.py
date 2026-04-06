class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = []
        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                prev_idx, _ = stack.pop()
                result[prev_idx] = i - prev_idx
            stack.append((i, temperature))

        return result
