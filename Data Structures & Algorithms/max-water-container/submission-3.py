class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Optimized
        maxwater=0
        L=0
        R=len(heights)-1

        while L<R:
            length=R-L
            height=min(heights[L], heights[R])
            water=length*height
            maxwater=max(maxwater, water)
            if(heights[L]<heights[R]):
                L +=1
            else:
                R -=1
        return maxwater

