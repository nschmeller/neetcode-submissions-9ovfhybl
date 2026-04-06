class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, left_bounds = [], [0] * len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left_bounds[i] = stack[-1] + 1
            stack.append(i)

        stack, right_bounds = [], [len(heights)] * len(heights)
        for i in reversed(range(len(heights))):
            while stack and heights[stack[-1]] > heights[i]:
                stack.pop()
            if stack:
                right_bounds[i] = stack[-1]
            stack.append(i)

        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area, heights[i] * (right_bounds[i] - left_bounds[i]))

        return max_area
