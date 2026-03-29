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
        while head1 and head2:

            sumofTwo=head1.val +head2.val+carry
            remainder=sumofTwo%10
            carry=sumofTwo//10
            
            newnode=ListNode(remainder)
            tail.next=newnode
            tail=tail.next

            head1=head1.next
            head2=head2.next

        while head1:
            sumofTwo=head1.val+carry
            remainder=sumofTwo%10
            carry=sumofTwo//10

            newnode=ListNode(remainder)
            tail.next=newnode
            tail=tail.next

            head1=head1.next

        while head2:
            sumofTwo=head2.val+carry
            remainder=sumofTwo%10
            carry=sumofTwo//10

            newnode=ListNode(remainder)
            tail.next=newnode
            tail=tail.next
            
            head2=head2.next

        if carry:
            newnode=ListNode(carry)
            tail.next=newnode
            tail=tail.next

        return dummy.next



           




