class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size=len(arr)
        maxsofar = arr[size-1]
        arr[size-1] = -1

        for i in range(size-2, -1, -1):
            curr = arr[i]
            arr[i] = maxsofar
            maxsofar =  max(maxsofar, curr)
        return arr
            