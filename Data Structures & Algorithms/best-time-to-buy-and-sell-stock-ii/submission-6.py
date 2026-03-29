class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # mem=defaultdict(int)
        n=len(prices)
        mem=[[0]*(n+1) for _ in range(2)] # we can do this way 
        # or we can also do this way with out inner for loop because we only
        # have two index 
        for j in range(n-1, -1, -1):
            mem[1][j]=max(mem[1][j+1], prices[j]+mem[0][j+1])
            mem[0][j]=max(mem[0][j+1], -prices[j]+mem[1][j+1])
                  
        return mem[0][0]