class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms=[[]]
        permset =set()
        for i in range(len(nums)):
            new_perms=[]
            for p in perms:
                for j in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(j, nums[i])
                    if tuple(p_copy) not in permset:
                     new_perms.append(p_copy)
                     permset.add(tuple(p_copy))

            perms = new_perms

        return perms
