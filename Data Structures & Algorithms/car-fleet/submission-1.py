class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair=[[p,s] for p, s in zip(position, speed)]
        stack=[]
        for p, s in sorted(pair)[::-1]:
            time_to_reach_dest=(target-p)/s # not ()//s becaue we need it to be in fraction
            stack.append(time_to_reach_dest)
            if len(stack)>=2 and stack[-2]>=stack[-1]: # because we need 2 elements to compare
                stack.pop()

        return len(stack)
