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
            res.append(ch)
            return
        for c in mydict[digits[i]]:
            dfs(i+1, ch+c)
        
     if digits:
         dfs(0, "")

     return res


