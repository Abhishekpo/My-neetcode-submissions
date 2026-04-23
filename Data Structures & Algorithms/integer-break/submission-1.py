class Solution:
    def integerBreak(self, n: int) -> int:
        maxvalue=0
        mem={1:1}
        def dfs(num):# the max product that we get after breaking num into positive integers >= 2

            if num in mem:
                return mem[num]
            
            maxvalue=0 if num==n else num
            for i in range(1, num):
                maxvalue=max(maxvalue, (i*(num-i)) , i*dfs(num-i))

            mem[num]=maxvalue
            return maxvalue

        return dfs(n)

