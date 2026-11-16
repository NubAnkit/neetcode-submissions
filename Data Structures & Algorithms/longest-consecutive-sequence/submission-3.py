class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        converted = set(nums)
        used = set()
        maxSize = i = 0
        while i < len(nums):
            currentVal = nums[i]
            size = 0
            if currentVal in used:
                i += 1
                continue 
            elif (currentVal - 1) not in converted:
                used.add(currentVal)
                size += 1
                currentVal += 1
                while (currentVal) in converted:
                    used.add(currentVal)
                    size += 1
                    currentVal += 1
            i += 1
            if size > maxSize: maxSize = size
        return maxSize