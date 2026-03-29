class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res=[]

        def dfs(i, list1):
            
            if(len(list1)==k):
                res.append(list1.copy())
                return
            
            for j in range(i, n+1):
                list1.append(j)
                dfs(j+1, list1)
                list1.pop()
        dfs(1, [])
        return res

