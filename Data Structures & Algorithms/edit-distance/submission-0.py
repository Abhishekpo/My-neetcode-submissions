class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        mem={}
        def dfs(i, j): # minimun number of operations to make the word1 starting at this position onwards

            if i>=len(word1): # we are appending all the character left after word1 finishes and if word2 left
                return len(word2)-j

            if j>=len(word2): # we are deleting all the characters and returning the number of operation needed when word2 finishes
                return len(word1)-i
            if (i,j) in mem:
                return mem[(i,j)]

            if word1[i]==word2[j]:
                result = dfs(i+1, j+1)

            else:
                delete=1+dfs(i+1, j)
                replace=1+dfs(i+1, j+1)
                add=1+dfs(i, j+1)

                result=min(delete, replace, add)
                mem[(i,j)]=result
                return result
                
            mem[(i,j)]=result
            return result

        return dfs(0,0)
                   