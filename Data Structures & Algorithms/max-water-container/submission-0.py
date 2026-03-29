class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left , right =0, len(heights)-1
        maxvol=0
        while left< right:
            height= min(heights[left], heights[right])
            area= right-left

            volume= height*area

            maxvol = max(maxvol, volume)
            if heights[left]<heights[right]:
                left +=1
            else:
                right -=1
        return maxvol
            
            