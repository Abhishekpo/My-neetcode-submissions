class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res=[]
        stack=[]

        def dfs(nopen, nclosed):

            if len(stack) == 2*n:
                res.append("".join(stack))
                return
            
            if nopen < n:
                stack.append("(")
                dfs(nopen+1, nclosed)
                stack.pop()
            
            if nclosed < nopen:
                stack.append(")")
                dfs(nopen, nclosed +1)
                stack.pop()
        dfs(0,0)
        return res