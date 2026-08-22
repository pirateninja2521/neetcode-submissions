# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        last = head
        for i in range(n):
            last = last.next
        
        toRemove = head
        prev = None
        while last:
            last = last.next
            prev, toRemove = toRemove, toRemove.next
        
        if not prev:
            return head.next
        else:
            prev.next = toRemove.next
        return head

        

        