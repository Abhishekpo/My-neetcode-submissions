class Solution:
    def trap(self, height: List[int]) -> int:
        maxheightleft=[0]* len(height)
        maxheightright=[0] *len(height)
        heightmin=[]
        left, right=0, len(height)-1
        result =0

        
        
        maxheightleft[left]=height[0]
        for i in range(1, len(height)):
            maxheightleft[i]=max(height[i], maxheightleft[i-1])

        maxheightright[right]=height[right]
        for i in range(len(height)-2, -1 ,-1):
            maxheightright[i]=max(height[i], maxheightright[i+1])
        
        for i in range(len(height)):
            heightdiff= min(maxheightleft[i], maxheightright[i])
            result += (heightdiff- height[i])

        return result


            


            
            