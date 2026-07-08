class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0

        l, r, maxProfit = 0, 1, 0

        while r < len(prices):
            if prices[l] <= prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
                r += 1
            else:
                l = r
        
        return maxProfit



            
          