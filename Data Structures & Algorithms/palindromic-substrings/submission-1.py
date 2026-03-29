class Solution:
    def countSubstrings(self, s: str) -> int:
        
        total=0

        #for odd length string
        for i in range(len(s)):
            l, r=i,i
            # this will count all the single and odd palindroms aaa, a, a, a = 4
            # eg = aba it will count a, b, a, abc total 4 not even will not run in this
            #case eg abba it will count a, b, b, a =4
            while l>=0 and r<len(s) and s[l]==s[r]: 

                l -=1
                r +=1
                total +=1
            # even length string
            # this will count all the even palindromes eg, aa_, _aa,  =2 total =6
            # eg, abba even will count bb, and bbaa =2  total =6
            l,r=i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                l -=1
                r +=1
                total +=1
        return total
