class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) %2 !=0:
            return False
        stack=[]
        for i in range(len(s)):
            if(s[i]=="("):
                stack.append(")")
            elif(s[i]=="{"):
                stack.append("}")
            elif(s[i]=="["):
                stack.append("]")
            else:
                if(len(stack) !=0 and stack.pop()==s[i]):
                    continue
                else:
                    return False
        return len(stack)==0 and s!=""
            
