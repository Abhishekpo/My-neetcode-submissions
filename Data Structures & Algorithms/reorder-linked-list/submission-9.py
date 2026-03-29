# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        list1=[]
        curr=head
     
        while curr:
            list1.append(curr)
            curr=curr.next
           
        i=0
        j=len(list1)-1

        while i<j:
            list1[i].next=list1[j]
            i+=1
            if i==j: # might be either i==j or i>=j 
                break 

            list1[j].next=list1[i]
            j-=1
        list1[i].next=None # has to make the last node next =null

        