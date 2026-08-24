# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2: 
            return None
        if not l1:
            return self.addTwoNumbers(l2, l1)
        # l1 not None
        if l2:
            head = ListNode()
            head.val = (l1.val + l2.val) % 10
            if not l1.next:
                if (l1.val + l2.val)//10:
                    l1.next = ListNode(val = 1)
            else:
                l1.next.val += (l1.val + l2.val)//10
            head.next = self.addTwoNumbers(l1.next, l2.next)
            return head
        elif l1.val >= 10:
            l1.val %= 10
            if not l1.next:
                l1.next = ListNode(val = 1)
            else:
                l1.next.val += 1
                l1.next = self.addTwoNumbers(l1.next, None)
            return l1
        else:
            return l1

