# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        length = 0
        temp = head

        #To find the length to get the half
        while temp:
            length += 1
            temp = temp.next
        
        half = length // 2

        #the first half
        arr = []
        while head and half  > 0:
            arr.append(head.val)
            head = head.next
            half -= 1

        #to get maximum
        maximum = 0
        while head:
            curr = head.val + arr[-1]
            maximum = max(maximum , curr)
            head = head.next 
            arr.pop()
        return maximum

        
        
        
        