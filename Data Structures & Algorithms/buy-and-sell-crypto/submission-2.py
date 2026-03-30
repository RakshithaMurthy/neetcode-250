class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minbuy = prices[0]

        for i in prices:
            maxprofit = max(maxprofit, i - minbuy)
            minbuy = min(minbuy,i)
        

        return maxprofit
        

        