class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}
        for i in range(len(nums)):
            want = target - nums[i]
            if want in sol.keys():
                ans = [i, sol[want]] if i < sol[want] else [sol[want], i]
                return ans
            else:
                sol[nums[i]] = i