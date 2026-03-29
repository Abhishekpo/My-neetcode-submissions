class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        mystack=[]
        res=0
        for token in tokens:
            if token=="+":
                ans=mystack.pop()
                res =ans +mystack.pop()
                mystack.append(res)
                    
            elif token=="-": # do this way to check the edge cases but the question says
            # there will at leat two operands at first so no need to handle the edge cases
                ans=mystack.pop()
                if mystack:
                    res =mystack.pop()-ans
                else:
                    res -= ans
                mystack.append(res)
                
            elif token=="*":
                ans =mystack.pop()
                res = mystack.pop() * ans
                mystack.append(res)

            elif token=="/":
                ans=mystack.pop()
                res= int(mystack.pop()/ans)
                mystack.append(res)

            else:
                mystack.append(int(token))

        return mystack[0]