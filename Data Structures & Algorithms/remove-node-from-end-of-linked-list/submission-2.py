# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        current=head
        length=0
        while current:
            length +=1
            current=current.next

        if length == n:
            return head.next
        
        delnode=length-n
        current2=head
        while delnode-1 >0 :
            current2=current2.next
            delnode -=1
        
        temp=current2.next
        if current2.next !=None:
            current2.next=current2.next.next
        else:
            head=temp
        return head
        



        
