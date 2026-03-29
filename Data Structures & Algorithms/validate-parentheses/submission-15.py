class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]
        for st in s:
            if st=="{":
                stack.append("}")
            elif st=="[":
                stack.append("]")
            elif st=="(":
                stack.append(")")
            else:
                if not (stack and stack.pop()==st):
                    return False

        return  False if stack else True