class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack=[]
        for a in asteroids: # looping through the astroids
          while stack and a<0 and stack[-1]>0: # collision happend if we have some element in the stack
                                               # and the current element is -ve and top of the stack is +ve
            diff=stack[-1]+a # collision 
            if diff >0: # meaning one in the stack is heavy destroy the current elem
                a=0
            elif diff <0: # meaning the current element is heavy or abs(value) is greater, so destroy top of the stack
                stack.pop()
            else: # meaning both are equal so destroy both
                a=0
                stack.pop()
          if a!=0: # meaning if a is not 0 and be a>0 or a<0 because a !=0 from the question
            stack.append(a)

        return stack

                

