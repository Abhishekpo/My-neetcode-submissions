class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        myhashmap={}
        for s in strs:
            sorteds=''.join(sorted(s))
            if sorteds not in myhashmap:
                myhashmap[sorteds]=[s]
            else:
                myhashmap[sorteds].append(s)

        return list(myhashmap.values())
        