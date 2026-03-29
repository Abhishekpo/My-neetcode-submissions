class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # the brute force would be using sorting
        res=[]
        myset=set()
        for i in range(len(strs)):
            sortedst="".join(sorted(strs[i]))
            if sortedst in myset:
                continue
            temp=[strs[i]]
            myset.add(sortedst)
            for j in range(i+1, len(strs)):
                if(sortedst=="".join(sorted(strs[j]))):
                    temp.append(strs[j])
            res.append(temp)
        return res
                
            
            



        
        