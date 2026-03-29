class Solution:
    def decodeString(self, s: str) -> str:
        
        stack=[]
        # dont over complicate everything think it simply and if you can't do that 
        # look at the solution
        for i in range(len(s)):
            if s[i] !="]":
                stack.append(s[i])
            else:
                st=""
                while stack[-1]!="[":
                    st = stack.pop() +st
                stack.pop()

                num=""
                while stack and stack[-1].isdigit(): # also we can do this isdigit()
                    num = stack.pop() +num
                stack.append(int(num)*st) # we can directly muliply like this 

        return "".join(stack)
            
            
                
                
            
        

        