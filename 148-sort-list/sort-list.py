# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_middle(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def merge(l1, l2):
            dummy = ListNode()
            curr = dummy
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

        if not head or not head.next:
            return head
        
        mid = get_middle(head)
        right = mid.next
        mid.next = None
        
        left_ = self.sortList(head)
        right_ = self.sortList(right)

        return merge(left_ , right_)