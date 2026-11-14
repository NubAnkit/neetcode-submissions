class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}
        for i in range(len(nums)):
            want = target - nums[i]
            if want in sol:
                return [sol[want], i]
            else:
                sol[nums[i]] = i