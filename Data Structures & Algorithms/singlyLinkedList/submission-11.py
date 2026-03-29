class Node:
    def __init__(self, val=None, next_node=None):
        self.val=val
        self.next= next_node

class LinkedList:
    
    def __init__(self):
        self.head=None
        self.tail=None
    
    def get(self, index: int) -> int:
        i=0
        curr=self.head
        while curr and i<index:
            curr=curr.next
            i+=1
        if(curr):
            return curr.val
        return -1

    def insertHead(self, val: int) -> None:
        newnode=Node(val)
        if self.head ==None:
            self.head=newnode
            self.tail=newnode
        else:
            curr=self.head
            newnode.next=curr
            self.head=newnode

    def insertTail(self, val: int) -> None:
        newnode=Node(val)
        if(self.tail==None):
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
        

    def remove(self, index: int) -> bool:
        i=0
        curr=self.head
        if(index==0 and curr):
            if(self.head==self.tail):
                self.head=None
            else:
                self.head=self.head.next
            return True


        while i<index-1  and curr:
            curr=curr.next
            i+=1
        if(curr and curr.next): # if this is false meaning we are at last index
                                #  so out of bound return false
            if(curr.next==self.tail): # this is for deleting 2ndlast node
                self.tail=curr
            curr.next=curr.next.next # this one work for everyone 

            return True

        return False

    def getValues(self) -> List[int]:
        newlist=[]
        curr=self.head
        while curr:
            newlist.append(curr.val)
            curr=curr.next
        return newlist
        
