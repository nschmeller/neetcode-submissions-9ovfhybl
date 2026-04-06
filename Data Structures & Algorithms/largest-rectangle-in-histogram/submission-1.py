class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, max_area = [], 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, higher = stack.pop()
                max_area = max(max_area, higher * (i - idx))
                start = idx
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area
