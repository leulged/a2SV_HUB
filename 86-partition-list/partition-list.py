# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_than = ListNode(-1)
        temp_less = less_than
        greater_than = ListNode(-1)
        temp_greater = greater_than
        while head:
            if head.val >= x:
                temp_greater.next = ListNode(head.val)
                temp_greater = temp_greater.next
            else:
                temp_less.next = ListNode(head.val)
                temp_less = temp_less.next
            head = head.next
        print(temp_less)
        greater_than = greater_than.next
        while greater_than:
            temp_less.next = ListNode(greater_than.val)
            temp_less = temp_less.next
            greater_than = greater_than.next
        
        return less_than.next

