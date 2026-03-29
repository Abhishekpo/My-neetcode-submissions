class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        L=0
        R=len(heights)-1
        maxarea=0
        while L<R:
            height=min(heights[L], heights[R])
            length=(R-L)
            area=height*length
            maxarea=max(maxarea, area)
            if heights[L]<=heights[R]:
                L+=1
            else:
                R -=1
            
        return maxarea
            

