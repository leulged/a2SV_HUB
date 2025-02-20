# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        length = 0
        if n == 1:
            prev = None
            if head.next is None:
                return 
            while temp.next:
                prev = temp
                
                temp = temp.next

            prev.next = None
            return head
        while temp:
            length += 1
            temp = temp.next

        pos = length - n
        curr = head
        if pos == 0:
            return head.next
        for _ in range(1,pos):
            curr = curr.next

        if curr and curr.next.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        return head
