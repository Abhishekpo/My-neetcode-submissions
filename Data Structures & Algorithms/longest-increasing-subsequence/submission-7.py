class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        mem=[-1]*n
        
        def dfs(i):
            if mem[i]!=-1:
                return mem[i]

            LIS = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))

            mem[i]=LIS
            return LIS

        return max(dfs(i) for i in range(n))