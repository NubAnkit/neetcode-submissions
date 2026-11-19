class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        final = 0
        minLeft = 101
        for i in prices:
            if i <= minLeft:
                minLeft = i
            elif (i - minLeft > final):
                final = i - minLeft
            else: 
                continue
        return final