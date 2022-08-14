# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#using slow and fast pointer approach  slow moves by 1 and fast moves by 2
#if slow reaches fast then then there is a loop as if there is no loop fast will reach a null before slow
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast =head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                break
        else:
            return None 
        #we don't have a cycle
        
        slow2=head
        # they will meet beacuse of the previus loop pointer the always meet at the end of the loop
        while slow2!=slow:
            slow2=slow2.next
            slow=slow.next
        return slow2