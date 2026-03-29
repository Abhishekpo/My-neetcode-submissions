class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mem=defaultdict(int)
        def dfs(i, bought):

            if(i>=len(prices)):
                return 0

            if mem[(i, bought)]:
                return mem[(i, bought)]

            res=dfs(i+1, bought)

            if bought:
                profit=prices[i]+dfs(i+1, False)
                res=max(res, profit)
            else:
                profit=-prices[i]+dfs(i+1, True)
                res=max(res, profit)
            mem[(i, bought)]=res
            return res
        return dfs(0, False)