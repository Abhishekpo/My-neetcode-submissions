class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Optimized 
        maxwater=0
        L=0
        R=len(heights)-1

        while L<R: # need to find the grater height poll at the farthest distance from itself 
                   # which might be either right or left and only increment the pointer 
                   # with the shorter height becaue shorter height changes the amount.
            length=R-L
            height=min(heights[L], heights[R])
            water=length*height
            maxwater=max(maxwater, water)
            if(heights[L]<heights[R]):
                L +=1
            else:
                R -=1
        return maxwater

