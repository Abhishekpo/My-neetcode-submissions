class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        L=0
        R=L+1
        profit=0
        while L<len(prices) and R<len(prices):
            buy=prices[L]
            sell=prices[R]
            
            if(sell<buy):
                L =R
                R +=1
            else:
                profit=max(sell-buy, profit)
                R +=1
        return profit
            
