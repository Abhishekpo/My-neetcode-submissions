class Solution:
    def isValid(self, s: str) -> bool:
        mystack=[]
        res=False
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
                 if len(mystack) !=0 and st == mystack.pop():
                    res=True
                 else:
                    return False
        if len(mystack) !=0:
            return False
        return res