# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge2Lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 or l2

        return dummy.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        N = len(lists)
        if N == 0:
            return None
        if N == 1:
            return lists[0]
        elif N == 2:
            return self.merge2Lists(lists[0], lists[1])
        else: # N >= 3:
            l1 = self.mergeKLists(lists[::2])
            l2 = self.mergeKLists(lists[1::2])
            return self.merge2Lists(l1, l2)
