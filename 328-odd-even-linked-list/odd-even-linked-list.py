# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode(-1)
        odd_curr = odd
        even = ListNode(-1)
        even_curr = even

        pos = 0
        
        while head:
            if (pos + 1) % 2 == 1:
                
                new_node = ListNode(head.val)
                odd_curr.next = new_node
                odd_curr = odd_curr.next
            else:
                new_node = ListNode(head.val)
                even_curr.next = new_node
                even_curr = even_curr.next
            pos += 1
            head = head.next
        
        while even.next:
            new_node = ListNode(even.next.val)
            odd_curr.next = new_node
            even = even.next
            odd_curr = odd_curr.next
        return odd.next