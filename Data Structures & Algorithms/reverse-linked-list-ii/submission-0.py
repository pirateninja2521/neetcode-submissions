# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        if left == right:
            return head
        
        dummy = ListNode(next = head)
        curr = last = dummy
        for i in range(left):
            last = curr
            curr = curr.next
        
        first = curr
        next = curr.next
        for i in range(right - left):
            nextnext = next.next
            next.next = curr
            curr, next = next, nextnext
        
        last.next = curr
        first.next = next
        return dummy.next
