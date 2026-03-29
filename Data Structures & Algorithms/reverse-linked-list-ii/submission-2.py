# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy=ListNode(-1)
        dummy.next=head
        curr=dummy
        PrevNode=None
        for i in range(left):
            PrevNode=curr
            curr=curr.next
        
        revPrev=None
        for i in range(right-left+1):
            temp=curr
            curr=curr.next
            temp.next=revPrev
            revPrev=temp
            
        PrevNode.next.next=curr
        PrevNode.next=revPrev

        return dummy.next


        

            