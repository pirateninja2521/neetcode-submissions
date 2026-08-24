# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nextChunkHead = head
        for i in range(k):
            if not nextChunkHead:
                # no k items left, return head directly
                return head
            nextChunkHead = nextChunkHead.next
        
        prev, curr = None, head

        for i in range(k):
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        
        head.next = self.reverseKGroup(nextChunkHead, k)
        return prev
