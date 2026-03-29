class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # newS=list() # the list will be empty so we cannot access news[i]
        # newT=list()
        # if len(s) != len(t) :
        #     return False

        # if s=="" and t=="":
        #     return True

        # for i in range(len(s)):
        #     newS.append(s[i])
        #     newT.append(t[i])

        # newS.sort()
        # newT.sort()

        # if(newS==newT):
        #     return True

        # return False

        if len(s) != len(t):
            return False
        
        return sorted(s)==sorted(t)