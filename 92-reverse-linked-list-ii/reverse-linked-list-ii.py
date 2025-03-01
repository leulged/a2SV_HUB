# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        curr = dummy
        n = 0

        while n < left - 1:
            curr = curr.next
            n += 1

        start = curr
        cur = curr.next

        prev = None
        while n < right:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            n += 1

        start.next.next = cur
        start.next = prev

        return dummy.next