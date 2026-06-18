class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        arr=[]
        def ispalindrome(st):
            L= 0
            R=len(st)-1
            
            while L < R:
                if st[L] != st[R]:
                    return False
                L +=1
                R -=1
            return True

        def dfs(i): # this says give me all the possible partiotioning starting from this index

            if i >=len(s):
                res.append(arr.copy())
                return
            
            for j in range(i, len(s)):
                piece = s[i:j+1] # performing the task for the partition part and 

                if ispalindrome(piece):
                    arr.append(piece)
                    dfs(j+1) # if left part is palindrom checking the same thing for remaining right part
                    arr.pop()
        dfs(0)
        return res

            

