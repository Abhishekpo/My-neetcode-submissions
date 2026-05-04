class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        r=0
        count =0
        l=0 
        while l < len(g):

            if r == len(s):
                return count

            if g[l] <= s[r]:
                count +=1
                l +=1

            r +=1

        return count
            
            
            
