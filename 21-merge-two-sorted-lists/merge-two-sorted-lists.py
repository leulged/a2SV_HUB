# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1)
        temp = ans

        while list1 and list2:
            if list1.val >= list2.val:
                temp.next = ListNode(list2.val)
                temp = temp.next
                list2 = list2.next

            else:
                temp.next = ListNode(list1.val)
                temp = temp.next
                list1 = list1.next

        while list1:
            temp.next = ListNode(list1.val)
            temp = temp.next
            list1 = list1.next

        while list2:
            temp.next = ListNode(list2.val)
            temp = temp.next
            list2 = list2.next
            
        return ans.next