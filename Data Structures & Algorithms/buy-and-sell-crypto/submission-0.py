class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        minVal = 101
        for i in prices:
            if i < minVal: minVal = i
            if i > minVal and i - minVal > bestProfit: bestProfit = i - minVal
        return bestProfit