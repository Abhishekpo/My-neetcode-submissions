class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem=[1e9]*(amount+1)
        mem[0]=0
        def dfs(amount):
            if mem[amount] !=1e9:
                return mem[amount]

            for coin in coins:
                if(amount-coin >=0):
                    mem[amount]=min(mem[amount], 1+mem[amount-coin])
            return mem[amount]
        for i in range(amount+1):
         mincoins=dfs(i)
        return -1 if mincoins >=1e9 else mincoins