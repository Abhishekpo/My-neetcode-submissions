class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        L=0
        size=0
        count=0
        hashset=set()
        for R in range(len(s)):
            if s[R] not in hashset:
                hashset.add(s[R])
            else:
               
                while s[R] in hashset and L<R:
                    hashset.remove(s[L])
                    L +=1
                hashset.add(s[R])

            count = max(count, len(hashset))
        return  count
        
            
                
            
