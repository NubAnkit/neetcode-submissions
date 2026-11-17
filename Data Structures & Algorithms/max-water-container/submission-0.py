class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l, r = 0, len(heights) - 1
        while l < r:
            cur = 0
            length = r - l
            if heights[l] <= heights[r]:
                cur = length * heights[l]
                l += 1
            elif heights[l] > heights[r]:
                cur = length * heights[r]
                r -= 1
            if cur > ans:
                ans = cur
        return ans
