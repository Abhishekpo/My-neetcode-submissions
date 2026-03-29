class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(start, end):
            L=start
            R=end
            while L<R:
                if(s[L]!=s[R]):
                    return False
                L +=1
                R -=1
            return True

        res=[]
        result=[]
        def dfs(i):
            
            if(i>=len(s)):
                result.append(res.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    res.append(s[i:j+1])
                    dfs(j+1)
                    res.pop()
        dfs(0)
        return result
            


                       