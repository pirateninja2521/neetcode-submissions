# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head or not head.next:
        #     return head

        # newHead = self.reverseList(head.next)

        # head.next.next = head
        # head.next = None

        # return newHead

        if not head: return None
        curr = head
        stack = []
        while curr != None:
            stack.append(curr)
            curr = curr.next
        
        while stack:
            if not curr:
                curr = stack.pop()
                head = curr
            else:
                curr.next = stack.pop()
                curr = curr.next
        curr.next = None
        return head