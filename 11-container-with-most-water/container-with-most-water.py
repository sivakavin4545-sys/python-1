class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maximum_water = 0

        while left < right:
            width = right - left
            container_height = min(height[left], height[right])

            maximum_water = max(
                maximum_water,
                width * container_height
            )

            # Move the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maximum_water