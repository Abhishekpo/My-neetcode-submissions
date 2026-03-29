class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        myset=set()
        def dfs(i, total, curr):

            if(i>=len(candidates) or total>target):
                return
            if(total==target):
                mytup=tuple(curr.copy())
                if mytup not in myset:
                    myset.add(mytup)
                return
                
            curr.append(candidates[i])
            dfs(i+1, total+candidates[i], curr)
            curr.pop()
            dfs(i+1, total, curr)

        dfs(-1,0,[])
        res=[]
        for c in myset:
            res.append(list(c))
        return res




            