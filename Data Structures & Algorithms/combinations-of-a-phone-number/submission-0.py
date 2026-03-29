class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
    
     mydict={
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mon",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz",
     }
     res=[]
     def dfs(i, ch):

        if(len(ch)==len(digits)):
            res.append("".join(ch))
            return

        for c in mydict[digits[i]]:
            ch.append(c)
            dfs(i+1, ch)
            ch.pop()
        
     if digits:
         dfs(0, [])

     return res


