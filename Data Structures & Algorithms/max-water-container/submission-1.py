class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l, r = 0, len(heights) - 1
        while l < r:
            width = r - l
            if heights[l] <= heights[r]:
                cur = width * heights[l]
                l += 1
            else:
                cur = width * heights[r]
                r -= 1
            if cur > ans:
                ans = cur
        return ans
