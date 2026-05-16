class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
       mydict = {}

       for i in range(len(order)):
         mydict[order[i]] = i 
       
       compare_with=words[0]
       for i in range(1, len(words)):
        L = 0
        R = 0

        comparing = words[i]
        while L < len(compare_with) and R < len(comparing):

            if mydict[compare_with[L]] > mydict[comparing[R]]:
                return False

            elif mydict[compare_with[L]] == mydict[comparing[R]]:
                L += 1
                R += 1

            else:
                break

        if L == len(comparing) and len(comparing) < len(compare_with):
            return False

        compare_with = comparing
            

        
       return True

        


       
       


