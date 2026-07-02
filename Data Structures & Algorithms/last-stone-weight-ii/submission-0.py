class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        total_stones = sum(stones)
        target = math.ceil(total_stones / 2)

        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (total_stones - total))

            if (i, total) in dp:
                return dp[(i,total)]
            
            dp[(i, total)] = min(dfs(i+1, total), dfs(i+1, total+stones[i]))

            return dp[(i, total)]
        dp={}
        return dfs(0, 0)
