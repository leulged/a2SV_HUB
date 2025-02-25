# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rev_l1 = l1
        rev_l2 = l2
        prev_l1 = None
        prev_l2 = None
        #to reverse the l1 and l2
        while rev_l1:
            next_node = rev_l1.next
            rev_l1.next = prev_l1
            prev_l1 = rev_l1
            rev_l1 = next_node
        l1 = prev_l1

        while rev_l2:
            next_node = rev_l2.next
            rev_l2.next = prev_l2
            prev_l2 = rev_l2
            rev_l2 = next_node
        l2 = prev_l2
        
        #joint of the linked list

        no1 = 0
        while l1:
            no1 = no1 * 10 + l1.val
            l1 = l1.next
        
        no2 = 0
        while l2:
            no2 = no2 * 10 + l2.val
            l2 = l2.next
        final_no = no1 + no2
        
        ans = ListNode(-1)
        nod = ans
        if  final_no == 0:
            nod.next = ListNode(0)
        while final_no != 0:
            curr = final_no % 10
            nod.next = ListNode(curr)
            nod = nod.next
            final_no //= 10

        return ans.next
        