class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
        what I am thinking is ,

lets say for now I dont know what dp is .

since Alice start first he chooses i index after that bob turn and he can choose i+1 and size-1 indices so he chooses max(i+1, size-1) and again Alice chooses max(i+1, size-2) if bob chooses last and max(i+2, size-1)

now I can see I can achieve that with some sort of recurssion not yet how.

state would definitely invlove index to know the turns since question says we have even number of piles meaning we will have size/2 turns each.


        """
        return True