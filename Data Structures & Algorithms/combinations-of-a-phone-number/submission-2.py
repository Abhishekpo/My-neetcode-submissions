class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        """
        so I have been give a digit for example 29
        so 2 => abc 3=> def and so on 
        now if I am given 34 then I need to generate all the possible combinations
        of that digit
        3=> def and 4=> ghi
        I need to generate all the letter combinations

        # how long the digits can be ? = 4
        # what if the digit is empty ? return []

        one thing I can think of is using for loop 
        for ch in def:
            for ch2 in ghi:
                newstr = ch+ch2
            ans.append(newstr)
        but what if I have 345 
        5=> jkl
        for 3 in str:
            for 4 , 5 in str 
        this will be complicated so rather I would use 
        use recursion

        """
        mydict = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        res =[]
        def dfs(i, arr):

            if i >= len(digits):
                res.append("".join(arr))
                return
            
            for ch in mydict[digits[i]]:
                arr.append(ch)
                dfs(i+1, arr)
                arr.pop()
        if digits:
         dfs(0, [])
        return res
        
