class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        pastA = None
        for a in range(len(nums) - 2):
            if pastA == nums[a]:
                continue
            b, c = a + 1, len(nums) - 1
            while b < c:
                target = -nums[a]
                curSum = nums[b] + nums[c]
                if curSum < target:
                    b += 1
                elif curSum > target:
                    c -= 1
                elif curSum == target:
                    if [nums[a], nums[b], nums[c]] not in ans:
                        ans.append([nums[a], nums[b], nums[c]])
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1
                    c -= 1
            pastA = nums[a]
        return ans
        