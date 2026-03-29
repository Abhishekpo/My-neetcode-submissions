class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # mem=defaultdict(int)
        n=len(prices)
        sellprofit=0
        buyprofit=0
        # we can do this way 
        # or we can also do this way with out inner for loop because we only
        # have two index 
        for j in range(n-1, -1, -1):
            temp=sellprofit
            sellprofit= max(sellprofit, prices[j]+buyprofit)
            buyprofit= max(buyprofit, -prices[j]+temp)
            

        return buyprofit