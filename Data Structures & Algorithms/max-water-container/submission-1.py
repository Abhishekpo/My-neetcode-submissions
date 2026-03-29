class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater=0
        for i in range(len(heights)):
         for j in range(i+1,len(heights)):
            length=j-i
            height=min(heights[i], heights[j])
            water=length*height
            maxwater=max(maxwater, water)
        return maxwater
