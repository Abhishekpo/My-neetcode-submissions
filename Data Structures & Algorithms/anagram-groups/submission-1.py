class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result=list()
        myset=set()
        for i in range(len(strs)):
            st=''.join(sorted(strs[i]))
            if st in myset:
                continue
            else:
                myset.add(st)

            mylist=[strs[i]]
            for j in range(i+1, len(strs)):
                if len(strs[i]) == len(strs[j]) and sorted(strs[i])==sorted(strs[j]):

                    mylist.append(strs[j])

            result.append(mylist)
        return result
            
        