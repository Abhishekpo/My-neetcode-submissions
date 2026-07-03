class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        prices = [1, 3, 4, 0, 4]
        if I buy then my next transactions has to be sell 
        I cant buy multiple times
        => buy when price is low and sell when high
        I have to buy at first so my first choice would be to buy any of the stock

        if I buy 1 and I have to sell now if it is higher
        if it is lower dont sell skip it 
        buy = False
        sell = False
        for i in range(len(prices)):
            
            if sell==False:
                buy = nums[i]
            if buy == True and sell 


        """
        mem = {}
        def dfs(i, holding):

            if i >= len(prices):
                return 0

            if (i, holding) in mem:
                return mem[(i, holding)]

            if holding:
                sell = prices[i] + dfs(i+2, False)
                skip = dfs(i+1, True)
                mem[(i,holding)] = max(sell,skip)
                return max(sell, skip)

            else:
                buy = -prices[i] + dfs(i+1, True)
                skip = dfs(i+1, False)
                mem[(i,holding)] = max(buy,skip)
                return max(buy, skip)

        return dfs(0, False)
                
            