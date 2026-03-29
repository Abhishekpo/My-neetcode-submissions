class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        newList=[]
        newset=set()
        for i in range(len(strs)):
            sorti=sorted(strs[i])
            if tuple(sorti) in newset:
                continue
            else:
             newset.add(tuple(sorti))
             ans=[strs[i]]
             hash1={}
             for s in strs[i]:
                hash1[s]=1+hash1.get(s, 0)
             for j in range(i+1, len(strs), 1):
                hash2={}
                for s in strs[j]:
                    hash2[s]=1+hash2.get(s, 0)
                
                if hash1==hash2:
                    ans.append(strs[j])
            newList.append(ans)
        return newList
                    
                
            
            
