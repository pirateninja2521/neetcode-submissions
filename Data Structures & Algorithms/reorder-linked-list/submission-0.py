# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        ptr = head
        secondPtr = self.reverseList(slow.next)
        slow.next = None

        while ptr and secondPtr:
            ptrNext = ptr.next
            secondPtrNext = secondPtr.next

            secondPtr.next = ptr.next
            ptr.next = secondPtr

            ptr, secondPtr = ptrNext, secondPtrNext
        

            

