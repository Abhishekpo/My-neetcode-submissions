class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        if sum(matchsticks) % 4 != 0:
            return False

        length = sum(matchsticks) //4

        side = [0]*4

        matchsticks.sort(reverse=True)
        

        def dfs(i): # check if we can generate square starting at index i 
            if i == len(matchsticks):
                return True
            
            for j in range(4):

                if side[j] + matchsticks[i] > length:
                    continue

                side[j] += matchsticks[i]

                if dfs(i+1):
                    return True

                side[j] -= matchsticks[i]

            return False

       
        return  dfs(0)



 