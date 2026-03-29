class Solution:
    def isValid(self, s: str) -> bool:
        
        my_stack=[]
        if len(s)%2 !=0:
            return False

        for ch in s:
            if ch =='(':
                my_stack.append(')')
            elif ch=='[':
                my_stack.append(']')
            elif ch=='{':
                my_stack.append('}')
            else:
                if my_stack and my_stack.pop()==ch:
                    continue
                else:
                    return False
                
        return True if not my_stack else False
                    
