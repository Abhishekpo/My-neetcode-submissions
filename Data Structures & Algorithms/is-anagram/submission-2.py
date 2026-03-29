class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) !=len(t):
            return False
        
        hashmap1={}
        hashmap2={}

        for e in s:
            hashmap1[e]= 1+ hashmap1.get(e,0)
        for e in t:
            hashmap2[e]= 1+ hashmap2.get(e,0)

        return hashmap1==hashmap2
        