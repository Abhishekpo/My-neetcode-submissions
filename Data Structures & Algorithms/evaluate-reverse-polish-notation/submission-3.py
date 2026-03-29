class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        mystack=[]
        res=0
        for token in tokens:
            if token=="+":
                ans=mystack.pop()
                if mystack:
                    res =ans +mystack.pop()
                else:
                    res += ans
                mystack.append(res)
                    

            elif token=="-":
                ans=mystack.pop()
                if mystack:
                    res =mystack.pop()-ans
                else:
                    res -= ans
                mystack.append(res)
                
            elif token=="*":
                ans =mystack.pop()
                if mystack:
                    res = mystack.pop() * ans
                else:
                    res *=ans
                mystack.append(res)

            elif token=="/":
                ans=mystack.pop()
                if mystack: 
                    res= int(mystack.pop()/ans)
                else:
                    res = int(res/ans)
                mystack.append(res)

            else:
                mystack.append(int(token))

        return mystack[0]