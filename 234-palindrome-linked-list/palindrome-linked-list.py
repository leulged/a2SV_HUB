# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = ListNode(head.val)
        temp_orig = head.next
        next_head = rev
        while temp_orig:
            next_head.next = ListNode(temp_orig.val)
            next_head = next_head.next
            temp_orig = temp_orig.next

        if head.next is None:
            return True
        temp = head
        prev = None

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        head = prev
        
        while head and rev:
            if prev.val != rev.val:
                return False
            prev = prev.next
            rev = rev.next
        return True
