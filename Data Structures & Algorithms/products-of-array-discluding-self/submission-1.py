class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        lr, rl = [1] * size, [1] * size
        i, k = 1, size - 2
        while i < size:
            lr[i] = lr[i - 1] * nums[i - 1]
            i += 1
        while k >= 0:
            rl[k] = rl[k + 1] * nums[k + 1]
            k -= 1
        return [a * b for a, b in zip(lr, rl)]
