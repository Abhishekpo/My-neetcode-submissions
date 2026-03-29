class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(i):

            if(len(nums)==i):
                return [[]]
            
            prems= dfs(i+1)
            local=[]
            for res in prems:
                for j in range(len(res)+1):
                    p=res.copy()
                    p.insert(j, nums[i])
                    local.append(p)
            return local
        return dfs(0)
        