class Solution:
    def isValid(self, s: str) -> bool:
        mystack=[]
        
        if len(s) %2 !=0:
            return False
        for st in s:
            if st=="[":
                mystack.append("]")
            elif st=="{":
                mystack.append("}")
            elif st=="(":
                mystack.append(")")
            else:
                 if not mystack or st != mystack.pop():
                    return False
                 
        return len(mystack)==0