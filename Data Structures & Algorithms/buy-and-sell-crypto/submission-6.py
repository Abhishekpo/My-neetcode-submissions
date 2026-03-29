class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy=prices[0]
        sell=0
        profit=0
        for p in prices:
            if p < buy:
                buy=p
            else:
                sell=p-buy
                profit=max(profit, sell)
        return profit