class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        lr = [1] * size
        i, k, right = 1, size - 2, 1
        while i < size:
            lr[i] = lr[i - 1] * nums[i - 1]
            i += 1
        while k >= 0:
            right = right * nums[k + 1]
            lr[k] *= right
            k -= 1
        return lr
