class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}
        for i in range(len(nums)):
            want = target - nums[i]
            if want in sol.keys():
                if i < sol[want]: return 
                sol = [i, sol[want]] if i < sol[want] else [sol[want], i]
                return sol
            else:
                sol[nums[i]] = i