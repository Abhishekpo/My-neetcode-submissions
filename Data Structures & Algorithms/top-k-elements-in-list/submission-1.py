class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mydic={}

        for num in nums:
            if num in mydic:
                mydic[num] +=1
            else:
                mydic[num] = 1
        
        sorted_dict = dict(sorted(mydic.items(), key=lambda item: item[1], reverse=True))

        key= list(sorted_dict.keys())
        
        return key[:k]
            
            

