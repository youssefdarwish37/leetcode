# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c,j=0,0
        a=head
        list2=ListNode()
        tail = list2
        while a:
            a=a.next
            c+=1
        while head:
            j+=1
            if(j>=(int(c/2)+1)):
                tail.next=head
                tail=tail.next
            head=head.next
            
        return list2.next
