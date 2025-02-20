# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        arr = set()
        temp = head
        while temp:
            if temp in arr:
                return temp
            arr.add(temp)
            temp = temp.next
        return 