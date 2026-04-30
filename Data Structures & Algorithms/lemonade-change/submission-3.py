class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        count=[0,0]
        for i in range(len(bills)):

            if bills[i] == 5:
                count[0] += 1

            if bills[i] > 5:
                if bills[i] == 10:
                    if count[0]:
                        count[0] -=1
                        count[1] += 1
                    else:
                        return False
                    
                else:
                    if count[0] and count[1]:
                        count[0] -=1
                        count[1] -=1
                    elif count[0]>2:
                        count [0] -=3
                    else:
                        return False


        return True
