class Solution:
    def integerBreak(self, n: int) -> int:
        # dfs(x) returns the maximum value we can get from x.
        # For the original number n, we MUST break it → so we start with res = 0.
        # For all smaller numbers (children), we MAY choose:
        #   - not break → value = x
        #   - or break further → try all splits
        # So res = x (don’t break) unless x == n.
        # Then we try all splits: dfs(i) * dfs(x - i),
        # which works because dfs(...) already decides whether to break or not.

        mem={}
        def dfs(num):
            if num == 1:
                return 1
            if num in mem:
                return mem[num]
            res = 0 if num == n else num # we give an option to not break if it is not the first elemet
            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                res = max(res, val)
            mem[num]=res
            return res

        return dfs(n)