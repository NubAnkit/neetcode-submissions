class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        size = len(nums)
        if size == 0:
            return False
        s = set()
        for i in nums:
            s.add(i)
        if size != len(s):
            return True
        return False