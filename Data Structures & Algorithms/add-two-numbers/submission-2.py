# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1=l1
        head2=l2
        carry=0
        dummy=ListNode(-1)
        tail=dummy
        while head1 or head2 or carry:

            firstlist=head1.val if head1 else 0 
            secondlist= head2.val if head2 else 0 
            sumofTwo=firstlist+secondlist +carry

            print(sumofTwo)
            remainder=sumofTwo%10
            carry=sumofTwo//10
            
            newnode=ListNode(remainder)
            tail.next=newnode
            tail=tail.next

            if head1:
             head1=head1.next

            if head2:
             head2=head2.next

       
        return dummy.next



           




