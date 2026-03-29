class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap=defaultdict(list)

        for st in strs:
            list1=[0]*26
            for s in st:
             list1[ord(s)-ord('a')] +=1
            list1=tuple(list1)
            hashmap[list1].append(st)

        return list(hashmap.values())



        