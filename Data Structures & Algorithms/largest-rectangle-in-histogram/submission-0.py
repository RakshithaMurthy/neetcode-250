class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Stack to store indices of the bars
        max_area = 0  # Variable to keep track of the maximum area
        heights.append(0)  # Append a zero height to flush out remaining bars

        for i in range(len(heights)):
            # While the current height is less than the height of the bar at the top of the stack
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]  # Pop the top index
                # Calculate the width
                w = i if not stack else i - stack[-1] - 1
                # Calculate the area with the popped height
                max_area = max(max_area, h * w)
            stack.append(i)  # Push the current index onto the stack

        return max_area